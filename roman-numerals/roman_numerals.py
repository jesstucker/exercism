def numeral(integer):
	integer = str(integer)
	def normalize(str_number):
		while len(str_number) % 4 != 0:
			str_number = '0' + str_number
		return str_number
	integer = normalize(integer)
	singles, tens, hundreds, thousands = integer[-1], integer[-2], integer[-3], integer[-4]
	singles_dict = {'0': '','1':'I','2':'II','3':'III','4':'IV','5':'V','6':'VI','7':'VII','8':'VIII','9':'IX'}
	tens_dict = {'0': '','1':'X','2':'XX','3':'XXX','4':'XL','5':'L','6':'LX','7':'LXX','8':'LXXX','9':'XC'}
	hundreds_dict = {'0': '','1':'C','2':'CC','3':'CCC','4':'CD','5':'D','6':'DC','7':'DCC','8':'DCCC','9':'CM'}
	thousands_dict = {'0': '','1':'M','2':'MM','3':'MMM'}
	return thousands_dict.get(thousands) + hundreds_dict.get(hundreds) + tens_dict.get(tens) + singles_dict.get(singles)