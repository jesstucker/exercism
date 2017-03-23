#SLO I KNO
#MUTATED 2

def sieve(limit):
	the_range = range(2, limit + 1)
	for number in the_range:
		slash = slasher(number, the_range)
		the_range = [x for x in the_range 
						if x not in slash]
	return the_range

def slasher(integer, lst):
	return [slashee for slashee in lst
				if slashee % integer == 0 
					and integer != slashee]