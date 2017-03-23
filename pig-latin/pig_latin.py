def translate(word):
	phrase = word.split()
	listo = []
	for word in phrase:
		if word.startswith('squ') or word.startswith('thr') or word.startswith('sch'):
			word = word[3:] + word[0:3] + 'ay'
			listo.append(word + ' ')
			continue
		if word.startswith('ch') or word.startswith('th') or word.startswith('qu'):
			word = word[2:] + word[0:2] + 'ay'
			listo.append(word + ' ')
			continue
		if word[0] in ['a','e','i','o','u','y','x']:
			if (word[0] == 'y' or word[0] == 'x') and word[1] in ['a','e','i','o','u','y']:
				word = word[1:] + word[0] + 'ay'
				listo.append(word + ' ')
				continue
			else:	
				word = word + 'ay'
				listo.append(word + ' ')
				continue
		else:
			word = word[1:] + word[0] + 'ay'
			listo.append(word + ' ')
	return ''.join(listo).strip()