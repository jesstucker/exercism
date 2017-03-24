#sofcobbled
#http://stackoverflow.com/questions/6701853/parentheses-pairing-issue
#never implemented a stack before
iparens = iter('(){}[]')
parens = dict(zip(iparens, iparens))
closing = parens.values()

def check_brackets(astr):
	stack = []
	for c in astr:
		d = parens.get(c, None)
		if d:
			stack.append(d)
		elif c in closing:
			if not stack: 
				return False #because no preceding open bracket
			# try:					#testing what .pop() would produce
			# 	to_pop = stack[-1]
			# except:
				# pass
			if c != stack.pop(): 
				return False # because resolved pair contains unresolved/wrong bracket
	return not stack #returns true if stack empty, all pairs "consumed", else unpaired brackets left in stack, which returns false