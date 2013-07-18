from watson import Tokenizer
import unittest


class TokenizerTest(unittest.TestCase):

	def test_tokenize(self):
		document = "Matrix of TelePresence components continue"
		tokens = Tokenizer.tokenize(document)

		self.assertEqual(len(tokens),3)