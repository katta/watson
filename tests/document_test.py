import unittest
import os

from tests.util import Util
from watson import Document


class DocumentTest(unittest.TestCase):

    def test_init(self):
        filepath = os.path.join(Util.content_dir_path(), "file1.txt")

        doc = Document(filepath)

        self.assertTrue(len(doc.text()) > 0)
        self.assertTrue(doc.text().find("people in charge") != -1)

    def test_init_with_txt(self):
        doc = Document("id", "txt")

        self.assertEqual(doc.text(), "txt")
        self.assertEqual(doc.id(), "id")

