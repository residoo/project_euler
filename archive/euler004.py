# euler004.py
# https://projecteuler.net/problem=4

"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 * 99.

Find the largest palindrome made from the product of two 3-digit numbers.

"""

# From 999 to 100, and from 999 to 100....

# IMPORTS

import math


# METHODS

def checkifpalindrome(number):
	isPalindrome = True				# We'll assume that it is...
	
	word = str(number)				# Turn number into a string for checking
	
	for i in range(int(len(word) / 2)):	# We're checking from both ends, so only need to go through half the word. This should round it up in case of uneven number of characters...
		if word[i] != word[len(word)-i-1]: # If the first isn't equal to the last, etc...
			isPalindrome = False			# then not a palindrome, sorry
			return isPalindrome
	
	return isPalindrome



# MAIN

iterations = 0
biggestPalindrome = 0

for i in range(999,100,-1):
	for j in range(999,100,-1):
		iterations += 1
		if checkifpalindrome(i*j):
			print "Palindrome found. " + str(i*j)
			print "The product of " + str(i) + " and " + str(j)
			print "This took " + str(iterations) + " iterations." 
			if i*j > biggestPalindrome:
				biggestPalindrome = i*j
			break
	

print "Biggest palindrome: " + str(biggestPalindrome)
