class Clock():
	def __init__(self, hours, minutes):
		self.hours = hours
		self.minutes = minutes
		self.cleanup()

	def __repr__(self):
		return "%02d:%02d" % (self.hours, self.minutes)

	def __eq__(self, other):
		return repr(self) == repr(other)

	def add(self, add_minutes)
		self.minute += add_minutes
		return self.cleaup()

	def cleaup(self):
		self.hour += self.minute // 60
		self.hour %= 24
		self.minutes %= 60
		return self