from collections import defaultdict
class WeighingMeasure():

    @classmethod
    def frequency_for(self, document_tokens):
    	term_frequency = defaultdict(long)
    	for token in document_tokens:
    		term_frequency[token] += 1
        return term_frequency
