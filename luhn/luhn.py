class Luhn(object):
	def __init__(self, number):
		self.number = number

	def is_valid(self):
		self.number = self.number.replace(' ','')
		if self.number.isdigit() == False or len(self.number) < 2:
			return False
		listo = []
		for each in self.number[-2::-2]:
			if (int(each) * 2) > 9:
				listo.append((int(each) * 2) - 9)
			else:
				listo.append(int(each) * 2)
		cc2 = [int(each) for each in self.number[-1::-2]]
		if (sum(listo) + sum(cc2)) % 10 == 0:
			return True
		else:
			return False