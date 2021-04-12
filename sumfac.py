#!/usr/bin/env python3

# Write a program that computes the running sum from 1..n
# Also, have it compute the factorial of n while you're at it
# No, you may not use math.factorial()
# Use the same loop for both calculations

n = 5

# your code goes here

def factorial(n):
	if n == 0:
		return 1
	prod = 1
	for i in range(1, n+1):
		prod = prod * i
	return prod
	
if __name__== '__main__':
	print(5, (n * (n + 1) // 2), factorial(n))
"""
python3 sumfac.py
5 15 120
"""
