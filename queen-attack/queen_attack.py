#https://youtu.be/mRntutn8udw
def board(w_queen,b_queen):
	validate(w_queen,b_queen)
	queenz = {(w_queen):'W',(b_queen):'B'}
	rowz = 0
	columnz = 0
	coordinates = {}
	blank_board = ['________'] *8
	for row in blank_board:
		for square in row:
			coordinates.update({((rowz, columnz)):square})
			columnz += 1
		rowz += 1
		columnz = 0

	coordinates.update(queenz)

	listo = []
	stringo = ''
	for k,v in sorted(coordinates.iteritems()):
		if k[1] == 7:
			stringo += v
			listo.append(stringo)
			stringo = ''
		else:
			stringo += v

	return listo


def can_attack(w_queen, b_queen):
	validate(w_queen,b_queen)
	wx,wy = w_queen[0], w_queen[1]
	bx,by = b_queen[0], b_queen[1]
	if wx == bx or wy == by:
		return True


	def diagonals((x,y)):
		a,b = x,y
		j,k = x,y
		dgnls = list()
		while x <= 7 and y <= 7:
			dgnls.append((x+1,y+1))
			x+=1
			y+=1
		while x >= 0 and y >= 0:
			dgnls.append((x-1, y-1))
			x-=1
			y-=1
		while a >= 0 and b <= 7:
			dgnls.append((a-1,b+1))
			a-=1
			b+=1
		while a <= 7 and b >= 0:
			dgnls.append((a+1, b-1))
			a+=1
			b-=1
		for each in dgnls:
			if each[0] < 0 or each[1] < 0:
				dgnls.remove(each)
			if each[0] > 7 or each[1] > 7:
				dgnls.remove(each)
			if each == (j,k):
				dgnls.remove(each)

		return set(dgnls)

	if w_queen in diagonals(b_queen) or b_queen in diagonals(w_queen):
		return True
	else:
		return False

def validate(w_queen,b_queen):
	if w_queen == b_queen:
		raise ValueError
	if w_queen[0] > 7 or w_queen[1] > 7 or b_queen[0] > 7 or b_queen[1] > 7:
		raise ValueError