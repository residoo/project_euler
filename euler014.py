# euler014.py
# https://projecteuler.net/problem=14

"""
LARGEST COLLATZ SEQUENCE

The following iterative sequence is defined for the set of positive integers:

n -> n/2 (n is even)
n -> 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:
13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1

It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.


"""


# IMPORTS

import math

# METHODS
	
def nextCStep(num):
	if num % 2 == 0:
		return num / 2
	else:
		return 3 * num + 1
	
# MAIN

num = 2
mostCSteps = 0
numberWithMostSteps = 0
ceiling = 1000000

for i in range(2,ceiling):
	num = i
	CSteps = 0
	while num != 1:
		num = nextCStep(num)
		CSteps += 1
	
	if CSteps > mostCSteps:
		mostCSteps = CSteps
		numberWithMostSteps = i
	
print
print		
print "The number with most steps was " + str(numberWithMostSteps) + " with " + str(mostCSteps) + " number of steps."