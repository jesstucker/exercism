SUBLIST, SUPERLIST, EQUAL, UNEQUAL = 1,2,3,4
def check_lists(list1, list2):
	if list1 == list2:
		return EQUAL
	if str(list1)[1:-1] in str(list2)[1:-1]:
		return SUBLIST
	elif str(list2)[1:-1] in str(list1)[1:-1]:
		return SUPERLIST
	else:
		return UNEQUAL