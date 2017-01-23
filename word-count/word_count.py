def word_count(text):
	import re
	from collections import Counter
	# text = text.replace("_"," ")
	# text = text.replace("!!&@$%^&","")
	# text = text.replace(":", "")
	text = text.replace('🖖'.decode('utf-8'), " ")

	text = text.replace("_", " ")
	text = re.sub(ur'\W', " ", text, flags=re.UNICODE)
	text = str.lower(text).split()
	return Counter(text)