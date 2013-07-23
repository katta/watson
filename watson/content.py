import os
from watson import Document
from collections import defaultdict

class Content():

    def __init__(self, path):
        self.path = path

    def all_documents(self):
        text_files = []
        documents = []

        for root, dirs, files in os.walk(self.path):
            text_files += map(lambda file: os.path.join(root, file), files)
        for filepath in text_files:
            documents.append(Document(filepath))
        return documents
