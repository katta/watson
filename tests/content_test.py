import unittest
import os

from watson import Content
from tests.util import Util


class ContentTest(unittest.TestCase):

    def test_all_documents(self):
        all_documents = Content(Util.content_dir_path()).all_documents()
        
        self.assertEqual(len(all_documents), 2)