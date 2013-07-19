import os
import importlib
not_init_and_pyc = lambda filneame: filename != "__init__.py" and not filename.endswith(".pyc")
test_files = []
for root, dirs, files in os.walk(os.path.dirname(os.path.abspath(__file__))):
    test_files += [filename.strip(".py") for filename in files if not_init_and_pyc(filename)]

for test_file in test_files:
    import_statement = "from tests.%s import *" % (test_file)
    exec (import_statement)