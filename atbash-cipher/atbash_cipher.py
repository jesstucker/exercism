import re
code_key = {'a': 'z', 'b': 'y', 'c': 'x', 'd': 'w', 'e': 'v', 'f': 'u', 'g': 't', 'h': 's', 'i': 'r', 'j': 'q', 'k': 'p', 'l': 'o', 'm': 'n', 'n': 'm', 'o': 'l', 'p': 'k', 'q': 'j', 'r': 'i', 's': 'h', 't': 'g', 'u': 'f', 'v': 'e', 'w': 'd', 'x': 'c', 'y': 'b', 'z': 'a'}

def decode(a_string):
	a_string = clean(a_string)
	return key_to_value(a_string)

def encode(a_string):
	return spaced(decode(a_string))

def spaced(a_string):
    return ' '.join(a_string[chunk:chunk+5] for chunk in range(0,len(a_string),5))

def clean(dirty):
	cleaned = (re.sub(r'\W', '', dirty))
	return cleaned.lower()

def key_to_value(a_string):
	return ''.join(code_key.get(each, each) for each in a_string)