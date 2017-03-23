#not great; pretty sloppy and cobbled
def slices(string, a_range):
	if len(string) < a_range:
		raise ValueError
	elif a_range == 0:
		raise ValueError
	else:
		container = []
		count = len(string)
		for each in string:
			if len(string) < a_range:
				break

			a_slice = string[0:a_range]
			formatted_slice = [int(part) for part in a_slice]
			container.append(formatted_slice)

			string = string[1:count]
			count -= 1
	return container