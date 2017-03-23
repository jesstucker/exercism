import math

def primitive_triplets(a):
	if a % 2 == 1:
		raise ValueError
	listo = []
	for b in range(1,45000):
		c = math.sqrt(a**2 + b**2)
		if c.is_integer():
			z = sorted((a,b,int(c)))
			listo.append(z)

	appendo = []
	for tuplo in listo:
		listy = []
		for each in tuplo:
			listy.append(set(prime_factors(each)))
		if bool(set(listy[0]) & set(listy[1]) & set(listy[2])) == False:
			appendo.append(tuple(tuplo))
		else:
			pass

	return set(appendo)

def triplets_in_range(mino, maxo):
	maxo = maxo + 1
	listo = []
	for a in range(mino,maxo):
		for b in range(mino,maxo):
			for c in range(mino,maxo):
				if a**2 + b**2 == c**2:
					x = sorted((a,b,c))
					listo.append(tuple(x))
	return set(listo)

def is_triplet(tupl):
	a,b,c = sorted(tupl)
	if a**2 + b**2 == c**2:
		return True
	else:
		return False

def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors