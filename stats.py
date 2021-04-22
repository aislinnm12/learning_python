#!/usr/bin/env python3

# Write a program that computes typical stats
# Count, Min, Max, Mean, Std. Dev, Median
# No, you cannot import the stats library!

import sys
import math




a = [3, 1, 4, 1, 5]
def condition(x):
	return x > 0
print("Count:", sum(condition(x) for x in a))

min = min(a)
print("Minimum:", min)

max = max(a)
print("Maximum:", max)

def averageoflist(a):
	sumOfNumbers = 0
	for t in a:
		sumOfNumbers = sumOfNumbers + t
	avg = sumOfNumbers / len(a)
	return avg
print("Mean:", averageoflist(a))



mean = sum(a)/len(a)
SUM =0
for i in a:
	SUM +=(i-mean)**2
stdeV = math.sqrt(SUM/(len(a)-1))
print("Std. dev:", (f'{stdeV:.3f}')

n = len(a)
a.sort()
  
if n % 2 == 0:
    median1 = n_num[n//2]
    median2 = n_num[n//2 - 1]
    median = (median1 + median2)/2
else:
    median = n_num[n//2]
print("Median: " + str(median))


#(f'{gc_count/len(dna):.2f}')
#for i in a():
#	print(a.count()
# list_name.count(a)


"""
python3 stats.py 3 1 4 1 5
Count: 5
Minimum: 1.0
Maximum: 5.0
Mean: 2.800
Std. dev: 1.600
Median 3.000
"""

