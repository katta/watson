import os
from watson import Tokenizer, WeighingMeasure


class Document():

    def __init__(self, path, txt=None):
        self.path = path
        self.tokens = []
        if txt is not None:
            self.content = txt
        else:
            with open(self.path) as file:
                self.content = file.read()

    def text(self):
        return self.content

    def id(self):
        return self.path

    def all_tokens(self):
        if len(self.tokens) > 0:
            return self.tokens
        self.tokens = Tokenizer.tokenize(self.content)
        return self.tokens

    def term_frequencies(self):
        return WeighingMeasure.term_frequency_for(self.all_tokens())