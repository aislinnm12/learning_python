#!/usr/bin/env python3

import random
random.seed(1) # comment-out this line to change sequence each time

# Write a program that stores random DNA sequence in a string
# The sequence should be 30 nt long
# On average, the sequence should be 60% AT
# Calculate the actual AT fraction while generating the sequence
# Report the length, AT fraction, and sequence

# cut -------------------------------------------------------------------------

bp = 30
seq = ''
at = 0
for i in range(bp):
	r = random.random()
	if   r < 0.30:
		seq += 'A'
		at += 1
	elif r < 0.50:
		seq += 'C'
	elif r < 0.70:
		seq += 'G'
	else:
		seq += 'T'
		at += 1

print(bp, at/bp, seq)

# cut -------------------------------------------------------------------------

"""
python3 at_seq.py
30 0.6666666666666666 ATTACCGTAATCTACTATTAAGTCACAACC
"""
