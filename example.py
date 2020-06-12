import spacy


nlp = spacy.load('en_core_web_sm')

from TextToCoNLL import text_to_conll

text_to_conll(text='He is walking on air. He is Michael Jordan.',
              nlp=nlp,
              delimiter="  ",
              output_dir='TextToConll/output',
              basename='example.conll',
              spacy_attrs=['text', 'lemma_', 'ent_type_'],
              default_values={'ent_type_': "O"},
              start_with_index=True,
              verbose=1)