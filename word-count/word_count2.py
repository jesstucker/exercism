from collections import Counter

def decode_if_needed(string):
	try:
		return string.decode('utf-8')
	except AttributeError:
		return string

def word_count(text):
	def replace_nonalpha(character):
		return character.lower() if chararcter.isalnum() else ' '
	text = ''.join(replace_nonalpha(c) for c in decode_if_needed(text))
	return Counter(text.split())




# def word_count(text):
# 	import re
# 	from collections import Counter

# 	text = text.replace('🖖'.decode('utf-8'), " ")

# 	text = text.replace("_", " ")
# 	text = re.sub(ur'\W', " ", text, flags=re.UNICODE)
# 	text = str.lower(text).split()
# 	return Counter(text)