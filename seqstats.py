#!/usr/bin/env python3

import argparse

# Write a program that computes statistics about a fasta file
#   Number of sequences
#   Total length
#   Minimum and maximum lengths
#   Average and median lengths
#   N50 length
# Use argparse
# Make useful functions and add them to your library

import argparse
import mcb185
import statistics

parser = argparse.ArgumentParser(desciption='stats about sequence')
#required arguments
parser.add_argument('--file', required=True, type=str, 
	metavar='<str>', help='required fasta file')
arg = parser.parse_args()

length = []
for name, seq in mcb185.read_fasta(arg.file):
	#print(name, len(seq))
	length.append(len(seq))
length.sort()
#print(length)

#MIN:
print('min is',min(length))

#MAX:
print('max is', man(length))

#sum:
#sum = 0
#for value in length:
#	sum += value
print('sum is', sum(length))

#mean
print('mean is', statistics.mean(length))

print('median is', statistics.median(length))

print('n50 is', mcb185.n50(arg.file))
#print(length)
#n50 - sum values, once it is greater than 1/2 the total sum, then that is the n50
running_sum = 0
total = sum(length)
for value in length:
	runnung_sum += value
	if running_sum > total/2:
		print('n50 is', value)
		break
