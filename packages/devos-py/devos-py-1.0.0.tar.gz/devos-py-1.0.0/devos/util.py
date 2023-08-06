from devos import prefixes
from nltk.tokenize import word_tokenize


def ordered_unique_list(items):
    """
    To get a unique list. This is similar to list(set(items)). But the difference is that it preserves the order
    source: https://stackoverflow.com/questions/480214/how-do-i-remove-duplicates-from-a-list-while-preserving-order
    """
    return list(dict.fromkeys(items))


def remove_quotes(keywords):
    return [k.replace('"', '') for k in keywords]


def get_possible_joins(tokens, joiners=[" "]):

    """
    Different characters to join the tokens
    """
    if len(tokens) == 1:
        return tokens

    poss = []  # possibilities
    for merged_tokens in get_possible_joins(tokens[1:], joiners=joiners):
        for j in joiners:
            t = tokens[0] + j + merged_tokens
            poss.append(t)
    return poss


def split_text(text):
    tokens = word_tokenize(text)
    return tokens


def split_text_manual(text, splitters=[" ", ".", ",", ":", "(", ")", ">", "<"]):
    if len(splitters) == 0:
        if text.strip() == "":
            return []
        return [text]
    sp = splitters[0]
    tokens = text.split(sp)
    tokens = [t for t in tokens if t.strip()!=""]
    toks = []  # tokenizes to the max
    for t in tokens:
        toks += split_text_manual(t, splitters[1:])
    return toks


def print_relations(relations):
    for r in relations:
        s, p, o = r
        print("%s  ----( %s )---->  %s" % (s, p, o))
