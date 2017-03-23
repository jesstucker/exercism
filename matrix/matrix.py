class Matrix(object):
	def __init__(self, string):
		self.string = string
	@property
	def rows(self):
		rows = [row.split() for row in self.string.split('\n')]
		return [[int(x) for x in row] for row in rows]
	@property
	def columns(self):
		rows = [row.split() for row in self.string.split('\n')]
		rows = [[int(x) for x in row] for row in rows]
		columns = zip(*[row for row in rows])
		return [list(column) for column in columns]