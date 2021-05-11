#!/usr/bin/env python3

import sys

# Write a program that predicts if a protein is trans-membrane
# Trans-membrane proteins have the following properties
#	Signal peptide: https://en.wikipedia.org/wiki/Signal_peptide
#	Hydrophobic regions(s): https://en.wikipedia.org/wiki/Transmembrane_protein
#	No prolines in hydrophobic regions (alpha helix)
# Hydrophobicity is measued via Kyte-Dolittle
#	https://en.wikipedia.org/wiki/Hydrophilicity_plot
# For our purposes:
#	Signal peptide is 8 aa long, KD > 2.5, first 30 aa
#	Hydrophobic region is 11 aa long, KD > 2.0, after 30 aa


ids = []
proteins = []

with open(sys.argv[1]) as fp:
	seq = []
	for line in fp.readlines():
		# print(line)
		line = line.rstrip()
		if line.startswith('>'):
			#print(line)
			words = line.split()
			ids.append(words[0][1:])
			if len(seq) > 0 : proteins.append(''.join(seq))
			seq=[]
		else:
			#print(line)
			seq.append(line)
	proteins.append(''.join(seq))
print(len(ids), len(proteins))

w=11
for id,seq in zip(ids,proteins):
	print(ids, len(seq))
	for i in range(len(seq)-w + 1):
		print(i, kd(seq[i:i+w]))


"""
python3 Programs/transmembrane.py Data/at_prots.fa
AT1G75120.1
AT1G10950.1
AT1G75110.1
AT1G74790.1
AT1G12660.1
AT1G75130.1
"""
