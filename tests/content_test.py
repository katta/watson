import unittest
import os
from watson import Content


class ContentTest(unittest.TestCase):

    def test_all_documents(self):
        tests_dir = os.path.dirname(os.path.abspath(__file__))
        content_dir = os.path.join(os.path.dirname(tests_dir), "content")
        all_documents = Content(content_dir).all_documents()
        
        self.assertEqual(len(all_documents), 2)