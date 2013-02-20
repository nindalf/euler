#!/usr/bin/env python3
"""
Searched online for a better way of knowing the index of the current iteration.
Found that the enumerate() function does just that. Updated a previous program
to use this.
An excellent pen and paper solution to this problem.
http://www.mathblog.dk/project-euler-25-fibonacci-sequence-1000-digits/

The old way to check if the element had 1000 digits.
divisor = 10**999
for index, element in enumerate(fibonacci()):
	if element >= divisor:
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
	for index, element in enumerate(fibonacci()):
		if len(str(element)) >= 1000:
			answer = index + 1 
			break
	print(answer)


if __name__ == "__main__":
	main()
