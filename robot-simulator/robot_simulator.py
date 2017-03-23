# with partial cheating, this one was a pleasure. proud of clean code.
NORTH = 0
EAST = 1
SOUTH = 2
WEST = 3
class Robot():
	def __init__(self, bearing=NORTH, x=0, y=0):
		self.bearing = bearing
		self.x = x
		self.y = y

	@property
	def coordinates(self):
		return (self.x,self.y)

	@property
	def bearing(self):
		return self.bearing

	def turn_right(self):
		self.bearing += 1
		if self.bearing > 3:
			self.bearing = self.bearing % 4

	def turn_left(self):
		self.bearing -= 1
		if self.bearing < 0:
			self.bearing = self.bearing % 4

	def adder(self, x, y):
		return tuple(map(sum, zip(self.coordinates, (x,y))))

	def advance(self):
		if self.bearing == NORTH:
			self.coordinates = self.adder(0,1)
		elif self.bearing == EAST:
			self.coordinates = self.adder(1,0)
		elif self.bearing == SOUTH:
			self.coordinates = self.adder(0,-1)
		elif self.bearing == WEST:
			self.coordinates = self.adder(-1,0)

	def simulate(self, orders):
		for order in orders:
			if order == 'L':
				self.turn_left()
			elif order == 'R':
				self.turn_right()
			elif order == 'A':
				self.advance()