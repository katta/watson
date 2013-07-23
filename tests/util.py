import os


class Util():

    @classmethod
    def content_dir_path(self):
		tests_dir = os.path.dirname(os.path.abspath(__file__))
		content_dir = os.path.join(os.path.dirname(tests_dir), "content")
		return content_dir
