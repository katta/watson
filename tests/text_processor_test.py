import unittest
from watson import TextProcessor


class TextProcessorTest(unittest.TestCase):

    def test_is_blank(self):
        text_processor = TextProcessor()
        self.assertTrue(text_processor.is_blank(""))
