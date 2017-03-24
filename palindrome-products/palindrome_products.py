#meh, weird first test
def largest_palindrome(max_factor, min_factor=0):
	listo = []
	lorange = range(min_factor+1, max_factor+1)
	for each in lorange:
		for seconds in lorange:
			produk = (each * seconds)
			product = str(produk)
			if product == product[::-1]:
				listo.append({produk:((each, seconds))})
	biggesto = max([each.keys()[0] for each in listo])
	justthebiggest = [each.values()[0] for each in listo if each.keys()[0] == biggesto]
	return biggesto, justthebiggest[0]


def smallest_palindrome(max_factor, min_factor=0):
	listo = []
	lorange = range(min_factor+1, max_factor+1)
	for each in lorange:
		for seconds in lorange:
			produk = (each * seconds)
			product = str(produk)
			if product == product[::-1]:
				listo.append({produk:((each, seconds))})
	smallesto = min([each.keys()[0] for each in listo])
	justthesmallest = [each.values()[0] for each in listo if each.keys()[0] == smallesto]
	return smallesto, justthesmallest[0]