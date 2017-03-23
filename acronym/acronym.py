import re
def abbreviate(phrase):
	phrase = re.sub('([A-Z]+)', r'-\1', phrase).replace('-',' ')
	string = ''
	for word in phrase.split():
		string += word[0]
	return string.upper()