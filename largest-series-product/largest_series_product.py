def largest_product(string_num, length):
	if string_num == '' and length > 0:
		raise ValueError
	if string_num == '' or length == 0:
		return 1
	if string_num.isdigit() == False or len(string_num) < length or length < 0:
		raise ValueError

	shitlist = []
	for product in string_num:
		shitlist.append(list(string_num[0:length]))
		string_num = string_num[1:]
		if len(string_num) < length:
			break

	shittierlist = [[int(string) for string in each] for each in shitlist]

	shittiestlist = []
	for each in shittierlist:
		shittiestlist.append(reduce(lambda x,y: x*y, each))

	return max(shittiestlist)