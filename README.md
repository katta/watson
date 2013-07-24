__Automatic Tagging Library__ for free text based on __Independent Component Analysis__ technique. 

[![Build Status](https://travis-ci.org/katta/watson.png?branch=master)](https://travis-ci.org/katta/watson)

### Setup

* Install Python 2.7.x
* Install virtualenv to manage packages

```bash
pip install virtualenv
virtualenv .env # this creates environment for this application
source .env/bin/activate 
```

* Install packages from eggs.txt

```bash
pip install -r eggs.txt
```

* Install nltk data packages, from python prompt execute these

```bash
python setup.py
```

### Usage

* After the setup you can run the following script against a document directory to generate most significant tags

```bash
./run.py <content directory path>
```

### Running Tests

Either use the helper script `./t` or run the command `python -m unittest -v tests`
