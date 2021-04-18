#!/usr/bin/env python3

# Write a program that computes the GC% of a DNA sequence
# Format the output for 2 decimal places
# Use all three formatting methods

dna = 'ACAGAGCCAGCAGATATACAGCAGATACTAT' # feel free to change

gc_count = 0
for i in range(len(dna)):
	if dna[i] == "C" or dna[i] == "G":
		gc_count += 1
print(f'{gc_count/len(dna):.2f}')
"""
python3 gc.py
0.42
0.42
0.42
"""
