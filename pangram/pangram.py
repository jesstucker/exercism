def is_pangram(sentence):
	sentence = str.lower(sentence)
	alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
	for letter in alphabet:
		if letter in sentence:
			pass
		else:
			return False
	return True