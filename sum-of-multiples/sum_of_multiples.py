def sum_of_multiples(limit, int_list):
	limit = range(1,limit)
	is_mult = []
	if 0 in int_list:
		int_list.remove(0)
	for each in limit:
		for integer in int_list:
			if each % integer == 0:
				is_mult.append(each)
	return sum(list(set(is_mult)))