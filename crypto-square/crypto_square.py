from math import sqrt, ceil
def encode(phrase):
    if not phrase:
        return ''
    cleaned = ''.join(filter(str.isalnum, phrase.lower()))
    cols = int(ceil(sqrt(len(cleaned))))
    return ' '.join([cleaned[c::cols] for c in range(cols)])