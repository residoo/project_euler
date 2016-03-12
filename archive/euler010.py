# euler010.py
# https://projecteuler.net/problem=10

"""

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.

"""

# IMPORTS

import math


# METHODS

def find_prime(num):
	isPrime = True

	if num % 10000 == 0:							# Just to show progress and judge speed...
		print "So far: " + str(num)
	
	if num > 1:
		for i in range(1,int(math.sqrt(num))):		# <--- VITAL. Otherwise it takes too damn long.
			if num % primes[i] == 0:
				isPrime = False
				break
	
	return isPrime

# MAIN

primes = [0]
sum = 0

for i in range(2,2000000):
	if find_prime(i):
		sum += i
		primes.append(i)
		
print sum