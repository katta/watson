from watson import Document, Timer
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

        timer = Timer()
        timer.start()
        print "\nBEGIN tokenizing for doc_id - %s" % (document.id())
        tokens = document.all_tokens()
        self.tokenized_docs[document.id()] = tokens
        print "FINISHED tokenizing in (%s) seconds" % (timer.lap())

        for token in tokens:
            self.all_tokens[token] += 1
        print "FINISHED calcluating term frequencies in (%s) seconds" % (timer.lap())

        for token in list(set(tokens)):
            self.doc_frequency[token] += 1
        print "FINISHED calcluating document frequencies in (%s) seconds" % (timer.lap())

        document_tf_vector = document.term_frequencies()
        self.document_tf_vectors.append(document_tf_vector)

        print "DONE tokenizing for doc_id - %s in (%s) seconds" % (document.id(), timer.end())

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
