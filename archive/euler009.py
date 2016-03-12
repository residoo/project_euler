# euler009.py
# https://projecteuler.net/problem=9

"""


A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a2 + b2 = c2

For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.

"""

# Solution is brute force.

# IMPORTS

import math


# METHODS

def checkIfSolution(a,b,c):
	solution = False
	
	if a < b and b < c:
		if math.pow(a,2) + math.pow(b,2) == math.pow(c,2):
			if a + b + c == 1000:
				solution = True
	
	return solution


# MAIN

a = 1
b = 2
c = 3

possibleC = []

for i in range(3,1000):
	possibleC.append(i)
	
for i in range(len(possibleC)):
	
	c = possibleC[i]
	
	for j in range(1,possibleC[i]):

		b = j
	
		for k in range(j):
		
			a = k
			
			if checkIfSolution(a,b,c):
				print "Solution found."
				print a*b*c
				quit()
			