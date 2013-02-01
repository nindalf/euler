import math
import timeit

"""
This method proved too slow. Better to set it to -1 rather than removing the value from the sieve list.
	try:
		sieve.remove(current)
	except ValueError:
		pass #its already been removed
"""

def eratosthenes(sieve, prime, limit):
	"""Removes multiples of the prime from the sieve."""
	current = 2*prime
	while current <= limit: 
		sieve[current] = -1
		current = current + prime


def prime_generator(limit = 100000):
	"""Yields a generator of prime numbers upto the limit."""
	sieve = [i for i in range(0, limit+1)]
	for i in sieve:
		if i > 1:
			eratosthenes(sieve, i, limit) 
			yield i


def main():
	dividend = 600851475143 #from the problem
	primelimit = math.floor(math.sqrt(dividend))
	for prime in prime_generator(primelimit):
		if dividend % prime == 0:
			answer = prime
	print("Divisble by", answer)


if __name__ == "__main__":
	main()
