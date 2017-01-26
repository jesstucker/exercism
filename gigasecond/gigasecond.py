from datetime import timedelta
def add_gigasecond(time):
	diff = timedelta(seconds=1000000000)
	return time + diff
	#EAF