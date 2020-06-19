import os

def text_to_conll(text,
                  nlp,
                  delimiter,
                  output_dir,
                  basename,
                  spacy_attrs,
                  default_values=dict(),
                  exclude=[],
                  start_with_index=True,
                  overwrite_existing_conll_file=False,
                  verbose=0):
    """

    :param str text: a string containing text
    :param nlp: spaCy model
    :param delimiter: the column delimiter
    :param str output_dir: the path to the output directory
    (will be created if it does not exists)
    :param str basename: the basename of the file
    i.e., the output will be written to output_dir/basename
    :param list spacy_attrs: a list of attributes of a token,
    i.e., for the token and the lemma ['text', 'lemma_']
    :param bool starts_with_index:
    if True, the first column is the token index of the token in the sentence
    :param dict default_values: a dictionary mapping the spaCy attr to a self-defined default value
e.g., {"ent_type_" : "O"}. The spaCy attribute has to be part of the argument "spacy_attrs".
    :param bool start_with_index: if True, the column is the index of the token in the sentence
    :param bool overwrite_existing_conll_file:
    if True and the basename already exists in the output folder, it will be overwritten
    if False and the basename already exists in the output folder, an Exception is raised.

    """
    if not os.path.exists(output_dir):
        os.mkdir(output_dir)
        if verbose >= 1:
            print(f'recreated the output dir at {output_dir}')

    output_path = os.path.join(output_dir, basename)

    for attr in default_values:
        assert attr in spacy_attrs, f'{attr} is not part of spacy_attrs, can not set default value.'

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

            excluded=False
            for attr_to_exclude in exclude:
                value = getattr(token, attr_to_exclude)
                if value:
                    excluded = True
            if excluded:
                continue

            info = []
            if start_with_index:
                info.append(str(index))

            for attr in spacy_attrs:

                if attr in default_values:
                    value = default_values[attr]
                else:
                    value = getattr(token, attr)
                info.append(value)

            the_line = delimiter.join(info) +'\n'
            outfile.write(the_line)

            needed = sum([start_with_index]) + len(spacy_attrs)
            observed = the_line.split(delimiter)
            assert len(observed) == needed, f'mismatch between required num of columns {needed} and observed {len(observed)}'

            index += 1









