#! /usr/bin/env python

import sys
from watson import Content

def run():

	if len(sys.argv) < 2 :
		print """Usage : ./run.py <Content Root Path>"""
		return -1

	content_root_path = sys.argv[1]
	content = Content(content_root_path)

	print len(content.all_documents())

if __name__ == "__main__" :
	run()
