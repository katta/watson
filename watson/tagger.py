from watson import Content, TextProcessor, WeighingMeasure
from collections import defaultdict


class Tagger():

    @classmethod
    def tag(self, path_to_document_root):
        text_processor = TextProcessor()
        content = Content(path_to_document_root)
        documents = content.all_documents()
      

    @classmethod
    def generate_using_ICA(self,document_to_tag,documents_in_corpus):
        pass
        # text_processor = TextProcessor()
        # tokens = text_processor.extract_nouns(document_to_tag)

        # tf_for_given_document = WeighingMeasure.term_frequency_for(tokens)
        # tf_across_documents = map(lambda document: UnigramDistribution.generate_tf_for_document(document),documents_in_corpus)
        # token_weight = defaultdict(float)
        # annotations = TagClass.objects(word__in=tokens)
        # for annotation in annotations:
        #     median_weight = annotation.term_frequency/float(annotation.document_frequency)
        #     list_of_deviation_square = map(lambda tf_hash: math.pow((tf_hash[annotation.word] - median_weight),2),tf_across_documents)
        #     token_weight[annotation.word] = tf_for_given_document[annotation.word] * math.sqrt(reduce(lambda x,y:x+y,list_of_deviation_square))
        # sorted_tag_tuples = map(lambda key: (key,token_weight[key]), sorted(token_weight,key=token_weight.get,reverse=True))
        # return sorted_tag_tuples[:10]