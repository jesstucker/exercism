def handshake(number):
	if isinstance(number, str):
		if any(int(c) in range(2,10) for c in number):
			return []
			
	if isinstance(number, int):
		if number > 0:
			number = bin(number)[2:]
		else:
			return []

	while len(number) < 5:
		number = '0' + number
 
	moves = []
	if number[-1] == '1':
		moves.append('wink')
	if number[-2] == '1':
		moves.append('double blink')
	if number[-3] == '1':
		moves.append('close your eyes')
	if number[-4] == '1':
		moves.append('jump')
	if number[-5] == '1':
		moves = moves[::-1]

	return moves

def code(listo):
	movs = ['wink','double blink','close your eyes', 'jump']
	points = [1,10,100,1000]
	moves = dict(zip(movs,points))
	if [i for i in listo if i not in moves.keys()]:
		return '0'

	index_run = [movs.index(each) for each in listo]
	is_reversed = index_run[0] > index_run[-1]

	if is_reversed:
		return str(10000 + sum([moves.get(i) for i in listo if i in moves]))
	else:
		return str(sum([moves.get(i) for i in listo if i in moves]))