#! /usr/bin/env python

import sys
from watson import Tagger

def run():

	if len(sys.argv) < 2 :
		print """Usage : ./run.py <Content Root Path>"""
		return -1

	content_root_path = sys.argv[1]
	# content = Content(content_root_path)
	tokenized_documents = Tagger.tag(content_root_path)

	for key,value in tokenized_documents.iteritems():
		print key, ":", value

if __name__ == "__main__" :
	run()
