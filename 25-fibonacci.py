#!/usr/bin/env python3
"""
Searched online for a better way of knowing the index of the current iteration.
Found that the enumerate() function does just that
"""
def fibonacci():
	current = 0 
	previous = 1
	yield previous
	while True:
		temp = current
		current = current + previous
		previous = temp
		yield current


def main():
	divisor = 10**999
	for index, element in enumerate(fibonacci()):
		if element >= divisor:
			answer = index 
			break
	print(answer)


if __name__ == "__main__":
	main()
