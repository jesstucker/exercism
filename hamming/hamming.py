def distance(DNA1, DNA2):
	if len(DNA1) != len(DNA2):
		raise ValueError
	DNA1_split = [nucleotide for nucleotide in DNA1]
	DNA2_split = [nucleotide for nucleotide in DNA2]
	pairing = zip(DNA1_split, DNA2_split)
	compair_pairings = [pair[0] == pair[1] for pair in pairing] #lol
	distance = compair_pairings.count(False)
	return distance