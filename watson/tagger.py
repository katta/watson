from watson import Content, TextProcessor, WeighingMeasure, Tokenizer
from collections import defaultdict
import math

class Tagger():

    @classmethod
    def tag(self, path_to_document_root):
        content = Content(path_to_document_root)
        documents = content.all_documents()
        document_tags = defaultdict(list)
        for doc_id, document in documents.iteritems() :
            tags = self.significant_tags_per_doc(document, documents)
            document_tags[doc_id] = tags            
        return document_tags
      

    @classmethod
    def significant_tags_per_doc(self,document_to_tag,documents_in_corpus):        
        tokens = Tokenizer.tokenize(document_to_tag)
        tf_for_given_document = WeighingMeasure.term_frequency_for(tokens)

        tokenized_documents = Tokenizer.tokenize_documents(documents_in_corpus)
        tf_across_documents = WeighingMeasure.term_frequencies_across(tokenized_documents) 
        document_frequencies = WeighingMeasure.document_frequency_for(tokenized_documents) 

        document_tf_vectors = []
        for doc_id, document in documents_in_corpus.iteritems():
            tokens = Tokenizer.tokenize(document)
            document_tf_vector = WeighingMeasure.term_frequency_for(tokens)
            document_tf_vectors.append(document_tf_vector)

        token_weight = defaultdict(float)        # annotations = TagClass.objects(word__in=tokens)
        for token in tokens :
            median_weight = tf_across_documents[token]/float(document_frequencies[token])  #TFIDF
            list_of_deviation_square = map(lambda tf_hash: math.pow((tf_hash[token] - median_weight),2),document_tf_vectors)
            token_weight[token] = tf_for_given_document[token] * math.sqrt(reduce(lambda x,y:x+y,list_of_deviation_square))
        sorted_tag_tuples = map(lambda key: (key,token_weight[key]), sorted(token_weight,key=token_weight.get,reverse=True))
        return sorted_tag_tuples[:10]