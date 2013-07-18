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
import nltk
nltk.download() # this opens downloader

## from Models tab download:
##   hmm_treebank_pos_tag, maxent_treebank_pos_tag
## from Corpora tab download:
##   wordnet

export NLTK_DATA <Path where the above packages are downloaded>
```

### Running Tests

Either use the helper script `./t` or run the command `python -m unittest -v tests`