from watson import TextProcessor
from collections import defaultdict

class Tokenizer():

    @classmethod
    def tokenize(self, document):
        return TextProcessor().extract_nouns(document)

    @classmethod
    def tokenize_documents(self, documents):
        tokenized_documents = defaultdict(list)
    	for doc_id, document in documents.iteritems():
        	tokens = self.tokenize(document)
        	tokenized_documents[doc_id] = tokens

    	return tokenized_documents
