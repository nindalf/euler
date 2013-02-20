#! /usr/bin/env python3

"""
Initial thoughts on this program:
Prime factorise every number, store the result in a dictionary.
Go through each dictionary and multiply them to generate the LCM.
This is very boring, however. In addition it consumes more time and memory.

Next thought:
LCM(a, b) = a*b/GCD(a,b)
There are efficient ways to compute GCD, ones that don't involve prime factorization.
Explanation of Euclid's algorithm - http://en.wikipedia.org/wiki/Euclidean_algorithm#Procedure

"""

def euclid_gcd(a, b):
	"""Implements Euclid's algorithm to find GCD."""
	x = max(a, b)
	y = min(a, b)
	while x%y > 0:
		temp = x%y
		x = y
		y = temp
	return y


def fast_lcm(a, b):
	return a*b/euclid_gcd(a,b)


def main():
	limit = 20
	lcm = 1
	for number in range(1, limit+1):
		lcm = fast_lcm(lcm, number)
	print(lcm)


if __name__ == "__main__":
	main()
