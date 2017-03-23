#highly unreadable SOFCOBBLE
#http://stackoverflow.com/questions/6800193/what-is-the-most-efficient-way-of-finding-all-the-factors-of-a-number-in-python
def divisor_generator(n):    
    return sorted(list(set(reduce(list.__add__, 
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))))[:-1]


def is_perfect(n):
	if n == (sum(divisor_generator(n))):
		return True
	else:
		return False