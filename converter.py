import os

def text_to_conll(text,
                  nlp,
                  output_dir,
                  basename,
                  spacy_attrs,
                  start_with_index=True,
                  overwrite_existing_conll_file=False,
                  verbose=0):
    """

    :param str text: a string containing text
    :param nlp: spaCy model
    :param str output_dir: the path to the output directory
    (will be created if it does not exists)
    :param str basename: the basename of the file
    i.e., the output will be written to output_dir/basename
    :param list spacy_attrs: a list of attributes of a token,
    i.e., for the token and the lemma ['text', 'lemma_']
    :param bool starts_with_index:
    if True, the first column is the token index of the token in the sentence
    :param bool overwrite_existing_conll_file:
    if True and the basename already exists in the output folder, it will be overwritten
    if False and the basename already exists in the output folder, an Exception is raised.

    """
    if not os.path.exists(output_dir):
        os.mkdir(output_dir)
        if verbose >= 1:
            print(f'recreated the output dir at {output_dir}')

    output_path = os.path.join(output_dir, basename)

    if all([not overwrite_existing_conll_file,
            os.path.exists(output_path)]):
        raise Exception(f'{output_path} already exists on disk.')

    doc = nlp(text)
    index = 1

    with open(output_path, 'w') as outfile:

        for token in doc:

            if all([token.is_sent_start,
                    token.i != 0]):
                outfile.write('\n')
                index = 1

            info = []
            if start_with_index:
                info.append(str(index))

            for attr in spacy_attrs:
                value = getattr(token, attr)
                info.append(value)

            outfile.write('\t'.join(info) +'\n')

            index += 1









