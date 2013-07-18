import unittest
from watson import WeighingMeasure


class WeighingMeasureTest(unittest.TestCase):

    def test_term_frequency_for(self):
        document_tokens = ["cisco", "router", "cisco", "switch"]

        frequencies = WeighingMeasure.term_frequency_for(document_tokens)

        self.assertEqual(len(frequencies.keys()), 3)
        self.assertEqual(frequencies["cisco"], 2)
        self.assertEqual(frequencies["router"], 1)

    def test_document_frequncy_measure_for(self):
        document1_tokens = ["cisco", "router", "cisco", "switch"]
        document2_tokens = ["network", "router", "cisco", "bridge", "voip"]
        tokenized_documents = {"doc1": document1_tokens, "doc2": document2_tokens}

        document_frequencies = WeighingMeasure.document_frequency_for(tokenized_documents)

        self.assertEqual(len(document_frequencies.keys()), 6)
        self.assertEqual(document_frequencies["cisco"], 2)
        self.assertEqual(document_frequencies["switch"], 1)
        self.assertEqual(document_frequencies["voip"], 1)

    def test_term_frequency_across(self):
        document1_tokens = ["cisco", "router", "cisco", "switch"]
        document2_tokens = ["network", "router", "cisco", "bridge", "voip"]
        tokenized_documents = {"doc1": document1_tokens, "doc2": document2_tokens}

        term_frequencies_across_docs = WeighingMeasure.term_frequencies_across(tokenized_documents)

        self.assertEqual(len(term_frequencies_across_docs.keys()), 6)
        self.assertEqual(term_frequencies_across_docs["cisco"], 3)
        self.assertEqual(term_frequencies_across_docs["router"], 2)
        self.assertEqual(term_frequencies_across_docs["switch"], 1)
