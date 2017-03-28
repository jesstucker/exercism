#oh my
#needs seriously refactoring lol
#moving on...
def board(b):
	#error checks
	equal_widths = all([len(row) == len(b[0]) for row in b])
	if equal_widths:
		pass
	else:
		raise ValueError

	border_chars = ['+','-','|']
	flats = b[0] + b[-1]
	walls = zip(*b)[0] + zip(*b)[-1]
	for plank in flats:
		if plank not in border_chars:
			raise ValueError
	for brick in walls:
		if brick not in border_chars:
			raise ValueError

	valid_inner_chars = [' ', '*']
	b_inner_chars = []
	for row in b[1:-1]:
		for char in row[1:-1]:
			b_inner_chars.append(char)

	for char in b_inner_chars:
		if char not in valid_inner_chars:
			raise ValueError


	#start main code
	coordinated = {}
	x,y = (0,0)
	for row in b[1:-1]:
		y = 0
		for square in row[1:-1]:
			coordinated.update({(x,y):square})
			y += 1
		x += 1


	def ac(tup,a,b):
		return (tup[0]+a,tup[1]+b)
	adjcoor = {}
	mines = {}
	for c,d in coordinated.iteritems():
		if d == '*':
			adjcoor.update({c:[ac(c,-1,-1),ac(c,0,-1),ac(c,1,-1),\
				ac(c,-1,0),ac(c,1,0),ac(c,-1,1),ac(c,0,1),ac(c,1,1)]})
			mines.update({c:d})


	# clean erroneous coordinates
	for k,v in adjcoor.iteritems():
		for coord in v:
			if coord[0] < 0 or coord[1] < 0:
				del v[v.index(coord)]
			if coord[0] > (len(b) - 3):
				try:
					del v[v.index(coord)]
				except:
					pass
			if coord[1] > (len(b[0]) - 3):
				try:
					del v[v.index(coord)]
				except:
					pass
			for mine in adjcoor.keys():
				if coord == mine:
					del v[v.index(coord)]

	# then do it twice because
	# it doesn't remove everything
	for k,v in adjcoor.iteritems():
		for coord in v:
			if coord[0] < 0 or coord[1] < 0:
				del v[v.index(coord)]
			if coord[0] > (len(b) - 3):
				try:
					del v[v.index(coord)]
				except:
					pass
			if coord[1] > (len(b[0]) - 3):
				try:
					del v[v.index(coord)]
				except:
					pass
			for mine in adjcoor.keys():
				if coord == mine:
					del v[v.index(coord)]

	# then do it three times because
	# it doesn't remove everything
	for k,v in adjcoor.iteritems():
		for coord in v:
			if coord[0] < 0 or coord[1] < 0:
				del v[v.index(coord)]
			if coord[0] > (len(b) - 3):
				try:
					del v[v.index(coord)]
				except:
					pass
			if coord[1] > (len(b[0]) - 3):
				try:
					del v[v.index(coord)]
				except:
					pass
			for mine in adjcoor.keys():
				if coord == mine:
					del v[v.index(coord)]

	#then do it four times because it doesn't remove everything
	# i know seriously
	for k,v in adjcoor.iteritems():
		for coord in v:
			if coord[0] < 0 or coord[1] < 0:
				del v[v.index(coord)]
			if coord[0] > (len(b) - 3):
				try:
					del v[v.index(coord)]
				except:
					pass
			if coord[1] > (len(b[0]) - 3):
				try:
					del v[v.index(coord)]
				except:
					pass
			for mine in adjcoor.keys():
				if coord == mine:
					del v[v.index(coord)]


	u_adj = []
	for k,v in adjcoor.iteritems():
		for adj in v:
			u_adj.append(adj)

	tallies = {each:u_adj.count(each) for each in u_adj}

	coordinated.update(mines)
	coordinated.update(tallies)


	column = 0
	stringo = '|'
	bun = '+{0}+'.format('-'*((len(b[0]) - 2)))
	listo = []
	listo.append(bun)
	for k,v in sorted(coordinated.iteritems()):
		if column == (len(b[0]) - 3):
			stringo += str(v)
			stringo += '|'
			listo.append(stringo)
			stringo = '|'
			column = 0
		else:
			stringo += str(v)
			column += 1
	listo.append(bun)


	return listo