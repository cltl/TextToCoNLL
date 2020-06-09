# Text to CoNLL using spaCy

The goal of this Python package is to convert
text to CoNLL using [spaCy](https://spacy.io/).

## Prerequisites
Python 3.6 was used to create this project. It might work with older versions of Python.

## Python modules

A number of external modules need to be installed, which are listed in **requirements.txt**.
Depending on how you installed Python, you can probably install the requirements using one of following commands:
```bash
pip install -r requirements.txt
```

## How to use
This repository is a package.
It can hence by imported as such from a parent folder of this package.

```python
from TextToCoNLL import text_to_conll
```

The function **text_to_conll** has the following arguments:
* text: the text to convert to CoNLL
* nlp: a spaCy model (result of using spacy.load)
* output_dir: the output directory
* basename: the basename of the output file
* spacy_attrs: the list of spaCy attrs to use a columns, e.g., ['text', 'lemma_']
* start_with_index: if True, the first column is the index
* overwrite_existing_conll_file: if False, do not allow do overwrite existing files
* verbose: if 1 or higher, logging information will be sent to stdout

Example (from a parent directory of this folder)

```python 
import spacy

nlp = spacy.load('en_core_web_sm')

from TextToCoNLL import text_to_conll

text_to_conll(text='He is walking on air. He is Michael Jordan.',
              nlp=nlp,
              output_dir='TextToConll/output',
              basename='example.conll',
              spacy_attrs=['text', 'lemma_'],
              start_with_index=True,
              verbose=1)
```

The output will be:

```bash
1	He	-PRON-
2	is	be
3	walking	walk
4	on	on
5	air	air
6	.	.

1	He	-PRON-
2	is	be
3	Michael	Michael
4	Jordan	Jordan
5	.	.
```

## Authors
* **Marten Postma** (m.c.postma@vu.nl)

## License
This project is licensed under the Apache 2.0 License - see the [LICENSE.md](LICENSE.md) file for details
