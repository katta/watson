from watson import Document
from collections import defaultdict


class Repository():

    def __init__(self):
        self.all_documents = defaultdict(Document)
        self.tokenized_docs = defaultdict(list)
        self.all_tokens = defaultdict(long)
        self.doc_frequency = defaultdict(long)
        self.document_tf_vectors = []

    def add(self, document):
        if self.all_documents.has_key(document.id()):
            raise RuntimeError("Document with %s already exists in Repository" % (document.id()))

        self.all_documents[document.id()] = document

        tokens = document.all_tokens()
        self.tokenized_docs[document.id()] = tokens

        for token in tokens:
            self.all_tokens[token] += 1

        for token in list(set(tokens)):
            self.doc_frequency[token] += 1

        document_tf_vector = document.term_frequencies()
        self.document_tf_vectors.append(document_tf_vector)

    def add_all(self, documents):
        for doc in documents:
            self.add(doc)

    def all_docs(self):
        return self.all_documents.values()

    def find_doc_by_id(self, doc_id):
        return self.all_documents[doc_id]

    def tokenized_documents(self):
        return self.tokenized_docs

    def term_frequencies_across_docs(self):
        return self.all_tokens

    def document_frequency(self):
        return self.doc_frequency

    def term_freqency_vectors(self):
        return self.document_tf_vectors
