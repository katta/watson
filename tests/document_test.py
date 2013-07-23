import unittest
import os

from watson import Document

class DocumentTest(unittest.TestCase):

    def test_init(self):
    	tests_dir = os.path.dirname(os.path.abspath(__file__))
        content_dir = os.path.join(os.path.dirname(tests_dir), "content")
    	filepath =  os.path.join(content_dir,"file1.txt")
    	
    	doc = Document(filepath)

    	self.assertTrue(len(doc.text()) > 0)
    	self.assertTrue(doc.text().find("people in charge") != -1)