# euler3.py
# https://projecteuler.net/problem=3

"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

# Will do this the hard way....

# First we make a list of all the prime numbers up to sqrt(600851475143) (is that possible?)

# IMPORTS

import math


# METHODS

def find_prime(num):
	isPrime = True

	if num > 1:	
		for i to range(2,num):
			if num % i == 0:
				isPrime = False
				break
	
	return isPrime



# MAIN

primes = [1]
num = 1

bigassnumber = 600851475143
ceiling = int(math.sqrt(bigassnumber))					# We don't need to check higher than this, right?
print "Ceiling: " + ceiling

for i to range(2,ceiling):
	num += 1
	if i < ceiling:
		if find_prime(num):
			primes.append(num)	
			print num,

print "We've found all the primes. Yay us."

print "Number of prime numbers: " + len(primes)
