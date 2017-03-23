def square_of_sum(n):
	the_sum = sum(each for each in range(1,n+1))
	the_square = the_sum ** 2
	return the_square

def sum_of_squares(n):
	the_natural_numbers = range(1,n+1)
	the_sum = sum([number ** 2 for number in the_natural_numbers])
	return the_sum

def difference(n):
	the_difference = square_of_sum(n) - sum_of_squares(n)
	return the_difference
