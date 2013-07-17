import os
from collections import defaultdict

class Content():

    def __init__(self, path):
        self.path = path

    def all_documents(self):
        text_files = []
        documents = defaultdict(str)
        for root, dirs, files in os.walk(self.path):
            text_files += map(lambda file: os.path.join(root, file), files)
        for filename in text_files:
            with open(filename) as file:
                documents[filename] = file.read()
        return documents
