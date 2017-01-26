#
# Skeleton file for the Python "Bob" exercise.
#
import re

def encoded_how(string):
	if isinstance(string, str):
		return string
 


def hey(what):
	what = what.rstrip()
	if what.endswith('.'):
		return 'Whatever.'
	elif what.endswith('?'):
		return 'Sure.'
	elif what == "":
		return 'Fine. Be that way!'


def check_if_yelling(raw_string):
	listified = [character for character in raw_string]
	take_alphas = [character for character in listified if u'character'.isalpha()]
	alpha_checklist = [True if u'character'.isupper() else False for character in take_alphas]
	if all(alpha_checklist):
		print "Whoa!"
	
