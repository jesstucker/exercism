from collections import defaultdict
#stolen, glossed over
class School(object):
	def __init__(self, name):
		self.name = name
		self.db = defaultdict(set)
	def add(self, student, level):
		self.db[level].add(student)
	def grade(self, level):
		return self.db[level]
	def sort(self):
		return ((grade, tuple(sorted(students)))
				for grade, students in self.db.items())
