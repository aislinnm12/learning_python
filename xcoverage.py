#!/usr/bin/env python3

# Write a program that simulates random read coverage over a chromosome
# Report min, max, and average coverage
# Make variables for genome size, read number, read length
# Input values from the command line
# Note that you will not sample the ends of a chromosome very well
# So don't count the first and last parts of a chromsome

import sys
import random


# like birthday problem

gen_size = []
read_num =[]
read_len = []

for j in range[read_num]:
		chrom = random.randint(0, read_len-1)
		gen_size[chrom] += 1
		
#for read_len in chrom:
#		if read_num > 1:
#			dup += 1
#			break
			
min = read_len[0]
max = read_len[-1]
avg = gen_size / read_len
print(min, max, avg)

"""
python3 xcoverage.py 1000 100 100
5 20 10.82375
"""
