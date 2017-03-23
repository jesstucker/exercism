def say(integer):
	integer = str(integer)
	integer = one_to_nineteen.get(integer)
	return integer


# def say(integer):
# 	#FML

# 	number = (normalize(list(str(integer))))

# 	tuple_grouping = zip(*(iter(number),) * 3)

# 	places = ['hundreds', 'thousand', 'million', 'billion'][::-1]

# 	dictionary = dict(zip(places, tuple_grouping))


	
# 	return dictionary


def normalize(data_list):
	while len(data_list) % 3 != 0:
		data_list = ['0'] + data_list
	while len(data_list) % 12 != 0:
		data_list = (['0']*3) + data_list
	return data_list

# def hundreds_sayer(dict_tuple):
# 	for each in dict_tuple:
# 		# print str(dict_tuple.get(each)) + each
# 		# print str(dict_tuple.get(each)) + each
# 		print each
# 		for tupl in dict_tuple.get(each):
# 			print tupl
# 			print type(tupl)

def hundreds_sayer(three_place_tuple):
	for place in three_place_tuple:
		


one_to_nineteen = {'1': 'one', '2': 'two','3': 'three','4': 'four','5': 'five','6': 'six','7': 'seven','8': 'eight','9': 'nine','10':'ten','11':'eleven','12':'twelve','13':'thirteen','14':'fourteen','15':'fifteen','16':'sixteen','17':'seventeen','18':'eighteen','19':'nineteen'}
# tens = {'20':'twenty','30':'thirty','40':'forty','50':'fifty','60':'sixty','70':'seventy','80':'eighty','90':'ninety'}
	# for each in say(1):
	# 	print str(say(1).get(each)) + each
