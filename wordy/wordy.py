import operator
def calculate(phrase):
	a_sign = {	'plus': operator.add,
				'minus': operator.sub,
				'multiplied':operator.mul,
				'divided':operator.div
	}
	phrase = phrase.replace('?','').split()
	parsed = []
	for each in phrase:
		if each.lstrip("-").isdigit():
			parsed.append(int(each))
		if each in a_sign:
			parsed.append(a_sign.get(each))

	chew = zip(parsed[2::2], parsed[1::2])
	init =  parsed[0]
	if not chew:
		raise ValueError

	for n,o in chew:
		try:
			init = o(init, n)
		except:
			raise ValueError

	return init