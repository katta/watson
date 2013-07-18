import unittest
from watson import WeighingMeasure


class WeighingMeasureTest(unittest.TestCase):

    def test_frequency_measure_for(self):
        document_tokens = ["cisco", "router", "cisco", "switch"]
        frequencies = WeighingMeasure.frequency_for(document_tokens)
        self.assertEqual(len(frequencies.keys()), 3)
