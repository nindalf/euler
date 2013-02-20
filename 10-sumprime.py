#! /usr/bin/env python3

"""
Yet another prime problem. I'll simply paste my Eratosthenes code and finish it.

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
	answer = 0	
	for prime in prime_generator(2000000):
		answer = answer + prime
	print(answer)

if __name__ == "__main__":
	main()
