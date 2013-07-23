from collections import defaultdict


class WeighingMeasure():

    @classmethod
    def term_frequency_for(self, document_tokens):
        term_frequency = defaultdict(long)
        for token in document_tokens:
            term_frequency[token] += 1
        return term_frequency

    @classmethod
    def document_frequency_for(self, tokenized_documents):
        document_frequency = defaultdict(long)
        for docid, tokens in tokenized_documents.iteritems():
            for token in list(set(tokens)):
                document_frequency[token] += 1
        return document_frequency
        
    @classmethod
    def term_frequencies_across(self, tokenized_documents):
        term_frequencies = defaultdict(long)
        for docid, tokens in tokenized_documents.iteritems():
            for token in tokens:
                term_frequencies[token] += 1
        return term_frequencies
