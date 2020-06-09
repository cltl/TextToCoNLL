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