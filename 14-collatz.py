#! /usr/bin/env python3
"""
Love this problem. Had a great time solving it.

"""

precomputed = {1: 1}

def collatz_successor(x):
	if x%2 == 0:
		return x/2
	else:
		return x*3 + 1


def collatz_length(x):
	if x in precomputed:
		return precomputed[x]
	else:
		successor = collatz_successor(x)
		computed_length = 1 + collatz_length(successor)
		precomputed[x] = computed_length
		return computed_length


def main():
	maximum = 1
	for i in range(1, 1000000):
		collatz_length(i)
		if precomputed[i] > precomputed[maximum]:
			maximum = i

	print(maximum, precomputed[maximum])

if __name__ == "__main__":
	main()
