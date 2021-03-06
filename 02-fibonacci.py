#! /usr/bin/env python3
"""
First time I used a generator in Python. Also took the opportunity to learn 
how iterators in general work.

"""

def fibonacci():
	current = 0
	previous = 1
	while True:
		temp = current
		current = current + previous
		previous = temp
		yield current


def main():
	answer = 0
	for element in fibonacci():
		if element%2 == 0:
			answer = answer + element
		if element > 4000000:
			break
	print(answer)


if __name__ == "__main__":
	main()
