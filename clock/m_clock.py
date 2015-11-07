class Clock:
	def __init__(self, hours, minutes):
		self.hours = hours
		self.minutes = minutes

	def __new__(self, hours, minutes):
		minutes = minutes % 1440
		hours = hours % 24
		overflow, minutes = divmod(minutes, 60)
		hours = hours + overflow
		time = (hours, minutes)
		time_formatted = "%02d"%hours + ":" + "%02d"%minutes
		return time_formatted

	def add(add_hours,add_minutes):
		sum_time = tuple(map(sum,zip(time,(add_hours,add_minutes)))) 
		return sum_time