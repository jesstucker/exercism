def is_isogram(word):
	False if word else True
	word = filter(str.isalpha, word.lower())
	listo = []
	for each in word:
		if each in listo:
			return False
		else:
			listo.append(each)
	return True