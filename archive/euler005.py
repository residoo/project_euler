# euler005.py
# https://projecteuler.net/problem=5

"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

# IMPORTS

import math


# METHODS

def isPrime(num): # Checks if "num" is a prime number. Returns True if it is.
	Prime = True
	
	if num > 1:
		for i in (range(2,num)):
			if (num % i) == 0:
				Prime = False
				break
	elif num == 1:
		Prime = True
	
	return Prime

	
def factorize(num):		# Pulls out the largest factor from num. Calls itself. We'll see.
	if num <= 1:
		return
	
	for i in (range(len(primes),0,-1)):
		if (num % primes[i-1] == 0):
			factors.append(primes[i-1])
			print num / primes[i-1]
			# raw_input("Press any key")
			factorize(num / primes[i-1])
			break
		
def countFactors(factors):	# Lets count factors

	for i in primes:
		count = 0
		for j in range(len(factors)):
			if factors[j] == i:
				count +=1
			
		if allfactors[i] < count:
			allfactors[i] = count
			
	

def checkifdivisible(number): # Checks if numbers is divisible with 1..20. Returns true if it is.
	divisible = True
	
	for i in range(20,0,-1):
		if number % i != 0:
			divisible = False
	
	return divisible

# MAIN

# Find all primes up to 20
primes = []

for i in range(1,20):
	if isPrime(i):
		primes.append(i)

print "We has primes."		
print primes
print

# Generate dictionary of all factors we'll be counting

allfactors = {}

for i in range(int(len(primes))+1):
	allfactors[primes[i-1]] = 0

print "We has factors."	
print allfactors
print

# Lets factorize something...

factors = []
temp = ""

for i in range(21):
	factorize(i)
	countFactors(factors)
	print factors
	# temp = raw_input("Press any key")
	factors = [] # Has to be reset.

	print
print "We has all the factors."
print allfactors

product = 1
count = 0

for i in allfactors:
	product *= i**allfactors[i]
	print i**allfactors[i]
	
print product

print checkifdivisible(product)

"""
ceiling = 4*5*6*7*9*11*13*14*17*19
divisible = 0
print checkifdivisible(ceiling)
print ceiling
"""

"""
for i in range(1,21):
	ceiling *= i
"""

"""
for i in range(ceiling,0,-1):
	print i
	if checkifdivisible(i):
		divisble = i
		break
"""

"""
found = False
i = 20

# DONT DO THIS
while not found:
	i += 20
	found = checkifdivisible(i)
	print i,
"""	
	

print
print "Score"
