#https://youtu.be/Xpugp6DIb3I?t=3m12s
reference = {' _ | ||_|   ': '0','     |  |   ':'1',\
	' _  _||_    ':'2',' _  _| _|   ':'3','   |_|  |   ':'4',\
	' _ |_  _|   ':'5',' _ |_ |_|   ':'6',' _   |  |   ':'7',\
	' _ |_||_|   ':'8',' _ |_| _|   ':'9'}
def number(str_list):
	for row in str_list:
		if len(row) % 3 != 0:
			raise ValueError
	if len(str_list) != 4:
		raise ValueError

	in_col = zip(*str_list)

	master = []
	num = []
	for n,row in enumerate(in_col,1):
		if n % 3 == 0:
			num.append(row)
			master.append(list(num))
			num = []
		else:
			num.append(row)

	tempstring = ''
	tempnum = ''
	to_digit = ''
	for number in master:
		for row in zip(*number):
			for char in row:
				tempstring += char
			tempnum += tempstring
			tempstring = ''
		to_digit += reference.get(tempnum, '?')
		tempnum = ''

	return to_digit

def grid(str_num):
	if str_num.isdigit():
		pass
	else:
		raise ValueError

	flipdict = {v:k for k,v in reference.iteritems()}
	linefeed = [numrow for num in [flipdict[num] for num in str_num] for numrow in num]

	stringo = ''
	fourths = range(0,12)[::3]

	for fourth in fourths:
		tw = 0
		for n in linefeed:
			stringo += ''.join(linefeed[fourth+tw:fourth+tw+3])
			tw += 12

	def group(iterator, count):
		itr = iter(iterator)
		while True:
			yield [itr.next() for i in range(count)]

	final = group(stringo,len(str_num * 3))
	return [''.join(row) for row in final]