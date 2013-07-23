class Repository():

    def __init__(self):
        self.all_documents = []

    def add(self, document):
		for doc in self.all_documents:
			if doc.id() is document.id():
				raise RuntimeError("Document with %s already exists in Repository" % (doc.id()))
		self.all_documents.append(document)

    def all_docs(self):
        return self.all_documents

    def find_doc_by_id(self, doc_id):
    	return next((d for d in self.all_documents if d.id() is doc_id) , None)
