import string
import random
reference = {'a':0,'b':1,'c':2,'d':3,'e':4,'f':5,'g':6,'h':7,'i':8,'j':9,'k':10,'l':11,'m':12,'n':13,'o':14,'p':15,'q':16,'r':17,'s':18,'t':19,'u':20,'v':21,'w':22,'x':23,'y':24,'z':25,}


class Cipher(object):
    def __init__(self, key=None):
    	if key == None:
    		self.key = ''.join([random.choice(string.ascii_lowercase) for each in range(100)])
    	else:
    		self.key = key

    	if self.key.isalpha() and self.key.islower():
    		pass
    	else:
    		raise ValueError

    def encode(self, phrase):
    	phrase = ''.join(filter(str.isalpha, phrase)).lower()
    	crap = ''

    	index = 0
    	for letter in phrase:	
    		if len(self.key) < index + 1:
    			index = 0
    			crap += chr(ord(letter) + reference.get(self.key[index]))
    		else:
    			crap += chr(ord(letter) + reference.get(self.key[index]))
    		index += 1	

    	crap2 = ''
    	for each in crap:
    		if ord(each) > 122:
    			crap2 += chr(ord(each) - 26)
    		else:
    			crap2 += each

    	return crap2

    def decode(self, encoded):
		crap = ''
		index = 0

		for letter in encoded:	
			if len(self.key) < index + 1:
				index = 0
				crap += chr(ord(letter) - reference.get(self.key[index]))
			else:
				crap += chr(ord(letter) - reference.get(self.key[index]))
			index += 1

		crap2 = ''
		for each in crap:
			if ord(each) < 97:
				crap2 += chr(ord(each) + 26)
			else:
				crap2 += each

		return crap2

class Caesar(object):
    def __init__(self):
    	pass
    def encode(self, phrase):
    	phrase = ''.join(filter(str.isalpha, phrase)).lower()
    	crap = ''
    	for letter in phrase:
    		if ord(letter) >= 120:
    			crap += chr(ord(letter) - 23)
    		else:
    			crap += chr(ord(letter) + 3)
    	return crap
    	
    def decode(self, phrase):
    	crap = ''
    	for letter in phrase:
    		if ord(letter) <= 97:
    			crap += chr(ord(letter) + 23)
    		else:
    			crap += chr(ord(letter) - 3)
    	return crap