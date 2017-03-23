import random, string
class Robot(object):
	def __init__(self):
		rc,rc2,ri,ri2,ri3 = random.choice(string.ascii_uppercase),\
							random.choice(string.ascii_uppercase),\
							random.choice(string.digits),\
							random.choice(string.digits),\
							random.choice(string.digits)
		self.nom = rc+rc2+ri+ri2+ri3

	@property
	def name(self):
		return self.nom

	def reset(self):
		random.seed(random.random())
		rc,rc2,ri,ri2,ri3 = random.choice(string.ascii_uppercase),\
							random.choice(string.ascii_uppercase),\
							random.choice(string.digits),\
							random.choice(string.digits),\
							random.choice(string.digits)
		self.nom = rc+rc2+ri+ri2+ri3
