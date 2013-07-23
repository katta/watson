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
    	for document in documents:
        	tokens = self.tokenize(document.text())
        	tokenized_documents[document.id()] = tokens

    	return tokenized_documents