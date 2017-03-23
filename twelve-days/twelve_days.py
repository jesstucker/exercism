positions = ['first','second','third','fourth','fifth','sixth','seventh','eighth','ninth','tenth','eleventh','twelfth']
days = dict(zip(range(1,13),positions))
review = ['twelve Drummers Drumming, ','eleven Pipers Piping, ','ten Lords-a-Leaping, ','nine Ladies Dancing, ','eight Maids-a-Milking, ','seven Swans-a-Swimming, ','six Geese-a-Laying, ','five Gold Rings, ','four Calling Birds, ','three French Hens, ','two Turtle Doves, ','and a Partridge in a Pear Tree.']
def verse(day):
	stringo = 'On the {0} day of Christmas my true love gave to me, '.format(positions[day-1])
	stringo2 = ''.join(review[abs(day - 12)::])
	if day == 1:
		stringo2 = stringo2.replace('and ', '')
	return stringo+stringo2+'\n'
def verses(day,to_day):
	return ''.join([verse(each)+'\n' for each in range(day,to_day+1)])
def sing():
	return verses(1,12)