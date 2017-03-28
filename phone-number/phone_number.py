class Phone(object):
	def __init__(self,number):
		self.number = filter(str.isdigit, number)
		if len(self.number) > 10:
			if self.number[0] == '1':
				self.number = self.number[1::]
			else:
				self.number = '0000000000'
		elif len(self.number) < 10:
			self.number = '0000000000'

	def area_code(self):
		return self.number[0:3]

	def pretty(self):
		return '({0}) {1}-{2}'.format(self.number[0:3],\
			self.number[3:6],self.number[6::])