from watson import Content, WeighingMeasure, Tokenizer, Repository
from collections import defaultdict
import math


class Tagger():

    def __init__(self):
        self.repository = Repository()

    def tag(self, path_to_document_root):
        content = Content(path_to_document_root)
        self.repository.add_all(content.all_documents())

        document_tags = defaultdict(list)
        for document in self.repository.all_docs():
            tags = self.significant_tags_per_doc(document)
            document_tags[document.id()] = tags
        return document_tags

    def significant_tags_per_doc(self, document_to_tag):
        tokens = document_to_tag.all_tokens()
        tf_for_given_document = document_to_tag.term_frequencies()
        tokenized_documents = self.tokenize_documents()

        tf_across_documents = WeighingMeasure.term_frequencies_across(tokenized_documents)
        document_frequencies = WeighingMeasure.document_frequency_for(tokenized_documents)

        document_tf_vectors = []
        for document in self.repository.all_docs():
            tokens = Tokenizer.tokenize(document.text())
            document_tf_vector = WeighingMeasure.term_frequency_for(tokens)
            document_tf_vectors.append(document_tf_vector)

        token_weight = defaultdict(float)
        for token in tokens:
            median_weight = tf_across_documents[token] / float(document_frequencies[token])  # TFIDF
            list_of_deviation_square = map(lambda tf_hash: math.pow((tf_hash[token] - median_weight), 2), document_tf_vectors)
            token_weight[token] = tf_for_given_document[token] * math.sqrt(reduce(lambda x, y: x + y, list_of_deviation_square))
            sorted_tag_tuples = map(lambda key: (key, token_weight[key]), sorted(token_weight, key=token_weight.get, reverse=True))
        return sorted_tag_tuples[:10]

    def tokenize_documents(self):
        tokenized_documents = defaultdict(list)
        for document in self.repository.all_docs():            
            tokenized_documents[document.id()] = document.all_tokens()

        return tokenized_documents