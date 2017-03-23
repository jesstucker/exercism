#head beating against wall to even get part of these idioms through
#my thick skull
class Allergies:
	_allergies = [
	'eggs',
	'peanuts',
	'shellfish',
	'chocolate',
	'tomatoes',
	'strawberries',
	'pollen',
	'cats']

	def __init__(self, score):
		self.score = score

	def is_allergic_to(self, allergy):
		return self.score & 1 << self._allergies.index(allergy)
	@property
	def lst(self):
		return [allergy for allergy in self._allergies
					if self.is_allergic_to(allergy)]