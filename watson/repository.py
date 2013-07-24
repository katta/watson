from watson import Document
from collections import defaultdict


class Repository():

    def __init__(self):
        self.all_documents = defaultdict(Document)

    def add(self, document):
        if self.all_documents.has_key(document.id()):
            raise RuntimeError("Document with %s already exists in Repository" % (document.id()))
        self.all_documents[document.id()] = document

    def add_all(self, documents):
        for doc in documents:
            self.add(doc)

    def all_docs(self):
        return self.all_documents.values()

    def find_doc_by_id(self, doc_id):
        return self.all_documents[doc_id]
