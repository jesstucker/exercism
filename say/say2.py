# def say(integer):
# 	#FML

# 	number = (normalize(list(str(integer))))

# 	tuple_grouping = zip(*(iter(number),) * 3)

# 	places = ['hundreds', 'thousand', 'million', 'billion'][::-1]

# 	dictionary = dict(zip(places, tuple_grouping))


	
# 	return dictionary

def say(integer):
	number = (normalize(str(integer)))
	return hundreds_sayer(number)


# def normalize(data_list):
# 	while len(data_list) % 3 != 0:
# 		data_list = ['0'] + data_list
# 	while len(data_list) % 12 != 0:
# 		data_list = (['0']*3) + data_list
# 	return data_list

def normalize(str_number):
	while len(str_number) % 3 != 0:
		str_number = '0'+str_number
	while len(str_number) % 12 != 0:
		str_number = '000'+str_number
	return str_number

def categorize():
	pass
# def hundreds_sayer(dict_tuple):
# 	for each in dict_tuple:
# 		# print str(dict_tuple.get(each)) + each
# 		# print str(dict_tuple.get(each)) + each
# 		print each
# 		for tupl in dict_tuple.get(each):
# 			print tupl
# 			print type(tupl)

def hundreds_sayer(threedigitstring):
	if threedigitstring[-2] == '0' or threedigitstring[-2] == '1':
		tens = one_to_nineteen.get(threedigitstring[0:2])
		singles = ''

	else:
		tens = tens_place.get(threedigitstring[-2])
		singles = one_to_nineteen.get(threedigitstring[-1], 'zero')
		if singles == 'zero':
			singles = ''
		else:
			singles = '-' + singles

	if threedigitstring[-3] == '0':
		hundreds = ''
	else:
		hundreds = one_to_nineteen.get(threedigitstring[-3]) + ' hundred '
	return hundreds + tens + singles
	


one_to_nineteen = {'1': 'one', '2': 'two','3': 'three','4': 'four','5': 'five','6': 'six','7': 'seven','8': 'eight','9': 'nine','10':'ten','11':'eleven','12':'twelve','13':'thirteen','14':'fourteen','15':'fifteen','16':'sixteen','17':'seventeen','18':'eighteen','19':'nineteen'}
tens_place = {'2':'twenty','3':'thirty','4':'forty','5':'fifty','6':'sixty','7':'seventy','8':'eighty','9':'ninety'}
	# for each in say(1):
	# 	print str(say(1).get(each)) + each
