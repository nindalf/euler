#! /usr/bin/env python3
"""
Important concept: DRY - Don't repeat yourself.
These 2 functions copied from problem 3.

Program improved after learning the enumerate() function.
Earlier the main() function looked like
index = 0
for prime in prime_generator():
	index = index + 1

The current method is more pythonic.
	
"""

def eratosthenes(sieve, prime, limit):
	"""Removes multiples of the prime from the sieve."""
	current = 2*prime
	while current <= limit: 
		sieve[current] = -1
		current = current + prime


def prime_generator(limit = 1000000):
	"""Yields a generator of prime numbers upto the limit."""
	sieve = [i for i in range(0, limit+1)]
	for i in sieve:
		if i > 1:
			eratosthenes(sieve, i, limit) 
			yield i


def main():
	for index, prime in enumerate(prime_generator()):
		if index == 10000: #index starts from 0
			answer = prime
	print("10001th prime -", answer)


if __name__ == "__main__":
	main()
