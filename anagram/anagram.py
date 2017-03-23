def detect_anagrams(match,list_of_words):
	if match == list_of_words[0]:
		return []
	else:
		return [each for each in list_of_words if sorted(match.lower()) == sorted(each.lower())]