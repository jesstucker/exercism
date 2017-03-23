#FML
b420 = {'1': 'one', '2': 'two','3': 'three','4': 'four','5': 'five','6': 'six','7': 'seven','8': 'eight','9': 'nine','10':'ten','11':'eleven','12':'twelve','13':'thirteen','14':'fourteen','15':'fifteen','16':'sixteen','17':'seventeen','18':'eighteen','19':'nineteen'}
tens_place = {'2':'twenty','3':'thirty','4':'forty','5':'fifty','6':'sixty','7':'seventy','8':'eighty','9':'ninety'}

def normalize(str_number):
	while len(str_number) % 3 != 0:
		str_number = '0'+str_number
	while len(str_number) % 12 != 0:
		str_number = '000'+str_number
	return str_number
	
def say(integer):
	if integer > 999999999999 or integer < 0:
		raise AttributeError
	if integer == 0:
		return "zero"

	number = (normalize(str(int(integer))))

	if number[0:3] == '000':
		billions = ''
	else:
		billions = hundreds_sayer(number[:3]) + ' billion '

	if number[3:6] == '000':
		millions = ''
	else:
		millions = hundreds_sayer(number[3:6]) + ' million '

	if number[6:9] == '000':
		thousands = ''
	else:
		thousands = hundreds_sayer(number[6:9]) + ' thousand '

	if number[9:] == '000':
		smalls = ''
	else:
		smalls = hundreds_sayer(number[9:])

	the_number =  billions + millions + thousands + smalls
	
	try:
		if the_number.strip().split()[-2] in ['billion','million','thousand']:
			the_number = billions + millions + thousands + 'and ' + smalls
			return the_number.strip()
		else:
			return the_number.strip()
	except IndexError:
		return the_number.strip()

def larger_than_tens(string):
	places = list(string[0:10])
	places = [int(each) for each in places]
	return any(places)	

def hundreds_sayer(string):
	# for 000
	if string[-3:] == '000':
		return ''
	# for 00n
	if string[-3:-1] == '00':
		singles = b420.get(string[-1] , 'h1')
		return singles
	# for n00
	if string[-2:] == '00' and string[-3] != '0':
		hundreds = b420.get(string[-3],)
		return hundreds + ' hundred'
	# for 0nn
	if string[-3] == '0' and string[-2] != '0' and string[-1] != '0':
		if string[-2:] in b420:
			tens = b420.get(string[-2:])
			return tens
		elif string [-2:] not in b420:
			tens = tens_place.get(string[-2])  + '-' + b420.get(string[-1])
			return tens
	# for 0n0
	if string[-3] == '0' and string[-2] != '0' and string[-1] == '0':
		if string[-2:] in b420:
			small = b420.get(string[-2:])
			return small
		elif string [-2:] not in b420:
			tens = tens_place.get(string[-2])
			return tens
	# for nnn
	if string[-3] != '0' and string[-2] != '0' and string[-1] != '0':
		hundreds = b420.get(string[-3])
		if string[-2:] in b420:
			tens = b420.get(string[-2:])
		elif string [-2:] not in b420:
			tens = tens_place.get(string[-2])  + '-' + b420.get(string[-1])
		return hundreds + ' hundred and ' + tens
	# for n0n
	if string[-3] != '0' and string[-2] == '0' and string[-1] != '0':
		hundreds = b420.get(string[-3])
		singles = b420.get(string[-1])
		return hundreds + ' hundred and ' + singles
	#for nn0
	if string[-3] != '0' and string[-2] != '0' and string[-1] == '0':
		hundreds = b420.get(string[-3])	
		if string[-2:] in b420:
			tens = b420.get(string[-2:])
		elif string [-2:] not in b420:
			tens = tens_place.get(string[-2])
		return hundreds + ' hundred and ' + tens