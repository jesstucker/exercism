#I get it. Tony Plog, etc..
def verse(number):
	if number > 2:
		plural = 's'
		line2 = "Take one down and pass it around, "
		subsequent = number-1
	elif number == 2:
		string = '2 bottles of beer on the wall, 2 bottles of beer.\nTake one down and pass it around, 1 bottle of beer on the wall.\n'
		return string
	elif number == 1:
		string = '1 bottle of beer on the wall, 1 bottle of beer.\nTake it down and pass it around, no more bottles of beer on the wall.\n'
		return string
	else:
		string = "No more bottles of beer on the wall, no more bottles of beer.\n"\
			"Go to the store and buy some more, "\
			"99 bottles of beer on the wall.\n"
		return string

	string = "{0} bottle{1} of beer on the wall, {2} bottle{3} of beer.\n"\
				"{4}"\
				"{5} bottle{6} of beer on the wall.\n".format(number, plural, number, plural, line2, subsequent, plural)

	return string

def song(high, low=0):
	return ''.join([verse(each)+'\n' for each in range(low,high+1)[::-1]])