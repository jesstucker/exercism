class Garden():
	def __init__(self, code, students=None):
		self.code = code.splitlines()
		if not students:
			self.students = ['Alice', 'Bob', 'Charlie', 'David','Eve', 'Fred', 'Ginny', 'Harriet','Ileana', 'Joseph', 'Kincaid', 'Larry']
		else:
			self.students = sorted(students)

	def plants(self, student):
		plant_ref = {'V': 'Violets', 'C':'Clover', 'R':'Radishes', 'G': 'Grass'}
		row1paired = [list(each) for each in zip(*2*[iter(self.code[0])])]
		row2paired = [list(each) for each in zip(*2*[iter(self.code[1])])]
		zipped = zip(row1paired, row2paired)

		listo = []
		for each in zipped:
			x = [plant_ref.get(plant) for plantgroup in each for plant in plantgroup]
			listo.append(x)

		reference = dict(zip(self.students, listo))
		result = reference.get(student)
		return result