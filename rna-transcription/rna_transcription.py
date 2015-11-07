def to_rna(DNA):
	transcript = {"G":"C", "C":"G","T":"A","A":"U"}
	RNA = [transcript.get(nucleotide) if nucleotide in transcript else "x" for nucleotide in DNA]
	if "x" in RNA:
		return ""
	else:
		return ''.join(RNA)
