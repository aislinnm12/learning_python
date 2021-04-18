#!/usr/bin/env python3

# Write a program that prints the reverse-complement of a DNA sequence
# You must use a loop and conditional

dna = 'ACTGAAAAAAAAAAA'

revcomp_dna = ''

for i in range(len(dna) -1, -1, -1):
	nt = dna[i]
	if 		nt == 'A' : nt = 'T'
	elif 	nt == 'T' : nt = 'A'
	elif	nt == 'C' : nt = 'G'
	elif	nt == 'G' : nt = 'C'
	else			  : nt = 'N'
	revcomp_dna += nt

comp_dna = ''

for i in reversed(range(len(dna))):
	nt = dna[i]
	if nt == 'A':
		c = 'T'
	elif nt == 'T':
		c = 'A'
	elif nt == 'C':
		c = 'G'
	else :
		c = 'C'
	comp_dna += c
print(comp_dna)

for nt in dna[::-1] : #from 0 to end of string, go by -1
	print(nt)


"""
python3 anti.py
TTTTTTTTTTTCAGT
"""
