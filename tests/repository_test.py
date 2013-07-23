import unittest
from watson import Document, Repository


class RepositoryTest(unittest.TestCase):

    def setUp(self):
        self.rep = Repository()

    def test_add_document(self):
        doc1 = Document("d1", "doc 1 text")

        self.rep.add(doc1)

        self.assertEqual(len(self.rep.all_docs()), 1)

        self.rep.add(Document("d2", "doc 2 text"))
        self.assertEqual(len(self.rep.all_docs()), 2)

    def test_add_only_if_does_not_exist(self):
        self.rep.add(Document("d1", "doc 1 text"))

        with self.assertRaises(RuntimeError):
            self.rep.add(Document("d1", "doc 1 text changed"))

    def test_find_doc_by_id(self):
        self.rep.add(Document("d1", "doc 1 text"))
        self.rep.add(Document("d2", "doc 2 text"))

        doc1 = self.rep.find_doc_by_id("d1")
        doc2 = self.rep.find_doc_by_id("d2")

        self.assertEqual(doc1.id(), "d1")
        self.assertEqual(doc2.text(), "doc 2 text")
        self.assertTrue(self.rep.find_doc_by_id("someid") is None)
