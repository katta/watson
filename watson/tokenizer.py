from watson import TextProcessor
class Tokenizer():

	@classmethod
	def tokenize(self, document):
		return TextProcessor().extract_nouns(document)
