def on_square(square_number):
	listo = []
	squarez = 1
	for step in range(square_number - 1):
		squarez = squarez * 2
	return squarez

def total_after(square_number):
	listo = []
	squarez = 1
	for step in range(square_number):
		listo.append(squarez)
		squarez = squarez * 2
	return sum(listo)