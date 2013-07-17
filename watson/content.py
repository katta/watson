import os


class Content():

    def __init__(self, path):
        self.path = path

    def all_documents(self):
        text_files = []
        documents = []
        for root, dirs, files in os.walk(self.path):
            text_files += map(lambda file: os.path.join(root, file), files)
        for filename in text_files:
            with open(filename) as file:
                documents.append(file.read())
        return documents
