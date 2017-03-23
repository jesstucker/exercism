def encode(string, rails):
	interval = (rails - 1) * 2
	resulto = ''
	for rail in range(rails):
		if rail % (rails - 1) == 0:
			resulto += string[rail::interval]
		else:
			innards = zip(string[rail::interval], list(string[interval-rail::interval]) + [''])
			resulto += ''.join(map(''.join, innards))
	return resulto

#LMAO
def decode(string, rails):
	string1 = encode(string,rails)
	string2 = string
	count = 0
	for each in range(69000):
		# print 'count',count,'result',string1,'LMAO'
		if string1 == string2:
			for each in range(count):
				string = encode(string,rails)
			return string
		else:
			string1 = encode(string1, rails)
			count += 1


'''
X.X.X.X.X.X.X.X.X.X.	1 +2
.X.X.X.X.X.X.X.X.X.X	2 +2


X...X...X...X...X...	1 +4
.X.X.X.X.X.X.X.X.X.X	2 +2
..X...X...X...X...X.	3 +4


X.....X.....X.....X.	1 +6
.X...X.X...X.X...X.X	2 +4+2
..X.X...X.X...X.X...	3 +2+4
...X.....X.....X....	4 +6


X.......X.......X...	1 +8
.X.....X.X.....X.X..	2 +6+2
..X...X...X...X...X.	3 +4+4
...X.X.....X.X.....X	4 +2+6
....X.......X.......	5 +8


X.........X.........	1 +10
.X.......X.X.......X	2 +8+2
..X.....X...X.....X.	3 +6+4
...X...X.....X...X..	4 +4+6
....X.X.......X.X...	5 +2+8
.....X.........X....	6 +10
'''