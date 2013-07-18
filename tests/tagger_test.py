from watson import Tagger
import os
import unittest


class TaggerTest(unittest.TestCase):

    def test_tag(self):
        tests_dir = os.path.dirname(os.path.abspath(__file__))
        content_dir = os.path.join(os.path.dirname(tests_dir), "content")
        document_tags = Tagger.tag(content_dir)

        for doc_id, tags in document_tags.iteritems():
            print "Doc Id [%s] Tags [%s]" % (doc_id, tags)
