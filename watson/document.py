import os


class Document():

    def __init__(self, path):
        self.path = path
        with open(self.path) as file:
            self.content = file.read()

    def text(self):
        return self.content

    def id(self):
        return self.path
