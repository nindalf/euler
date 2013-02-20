#!/usr/bin/env python3

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
	divisor = 10**1000
	for index, element in enumerate(fibonacci()):
		if element//divisor > 0:
			print(element)
			answer = index 
			break
	print(answer)


if __name__ == "__main__":
	main()
