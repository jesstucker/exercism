def transform(dic):
	dicto = {}
	for key,value in dic.iteritems():
		for each in value:
			dicto[each.lower()] = key
	return dicto