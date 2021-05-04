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

gen_size = int(sys.argv[1])
read_num = int(sys.argv[2])
read_len = int(sys.argv[3])



# create empty genome

chrom = [0] * gen_size



# fill up genome with random reads

for i in range(read_num):
	start = random.randint(0, gen_size-read_len)
#	print(start)
	end = start + read_len
	for coor in range(start, end):
		chrom[coor] += 1
	
print(chrom)



# look for min, max, and avg
min_len = 9999
minim = []
for i in range(+read_len, -read_len):
	if read_len(i) < min_len:
		min_len = read_len(i)
		minim = i 
	

print(minim, read_num, read_len)






"""
python3 xcoverage.py 1000 100 100
5 20 10.82375
"""
