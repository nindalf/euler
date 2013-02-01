import math


def eratosthenes(sieve, prime):
	"""Removes multiples of the prime from the sieve."""
	current = 2*prime
	while current <= sieve[-1]:
		try:
			sieve.remove(current)
		except ValueError:
			pass #its already been removed
		current = current + prime


def prime_generator(limit = 1000000):
	"""Yields an iterator of prime numbers upto the limit."""
	sieve = [i for i in range(2, limit+1)]
	for i in sieve:
		eratosthenes(sieve, i) 
		yield i


def main():
	dividend = 600851475143 #from the problem
	primelimit = math.floor(math.sqrt(dividend))
	primelimit = 1000000
	for prime in prime_generator(primelimit):
		if dividend % prime == 0:
			answer = prime
			print(answer)



if __name__ == "__main__":
	main()
