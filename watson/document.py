import os


class Document():

    def __init__(self, path, txt=None):
        self.path = path
        if txt is not None:
            self.content = txt
        else:
            with open(self.path) as file:
                self.content = file.read()

    def text(self):
        return self.content

    def id(self):
        return self.path
