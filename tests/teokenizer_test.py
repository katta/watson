from watson import Tokenizer
import unittest


class TokenizerTest(unittest.TestCase):

	def test_tokenize(self):
		document = "Matrix of TelePresence components continue"
		tokens = Tokenizer.tokenize(document)

		self.assertEqual(len(tokens),3)

	def test_tokenize_documents(self):
		document1 = "Matrix of TelePresence components continue"
		document2 = "This Table provides a description of various TelePresence components like voip."
		all_documents = {"doc1":document1,"doc2":document2}
		tokenized_documents = Tokenizer.tokenize_documents(all_documents)

		self.assertEqual(len(tokenized_documents.keys()),2)
		self.assertEqual(len(tokenized_documents["doc1"]),3)				
		self.assertEqual(len(tokenized_documents["doc2"]),4)