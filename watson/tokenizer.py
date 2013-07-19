from watson import TextProcessor
from collections import defaultdict

class Tokenizer():

    @classmethod
    def tokenize(self, document):
        tokens = TextProcessor().extract_nouns(document)
        return map(lambda token: token.lower(), tokens)        

    @classmethod
    def tokenize_documents(self, documents):
        tokenized_documents = defaultdict(list)
    	for doc_id, document in documents.iteritems():
        	tokens = self.tokenize(document)
        	tokenized_documents[doc_id] = tokens

    	return tokenized_documents