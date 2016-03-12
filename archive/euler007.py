# euler007.py
# https://projecteuler.net/problem=7

"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?

"""

# IMPORTS

import math


# METHODS

def find_prime(num):
	isPrime = True

	if num % 1000 == 0:
		print "So far: " + str(num)
	
	if num > 1:
		for i in primes:	# <--- VITAL. Otherwise it takes too damn long.
			if (num % i) == 0:
				isPrime = False
				break
	
	return isPrime



# MAIN

primes = [2]
num = 2
numberofprimes = 1

while numberofprimes < 10001:
	num += 1
	if find_prime(num):
		primes.append(num)	
		numberofprimes += 1

print "We've found all the primes. Yay us."

print numberofprimes
print primes[numberofprimes-1]
print primes