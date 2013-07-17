from watson import Content, TextProcessor
from collections import defaultdict

class Tagger():

	@classmethod
	def tag(self,path_to_document_root):
		text_processor = TextProcessor()
		content = Content(path_to_document_root)
		documents = content.all_documents()
		tokenized_documents = defaultdict(list)
		for filename, document in documents.iteritems():
			tokens = text_processor.extract_nouns(document)
			tokenized_documents[filename] = tokens

		return tokenized_documents
