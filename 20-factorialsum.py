#! /usr/bin/env python3

"""
Very easy problem to solve in python because there is no limit on the number of
digits in an integer. Further computing 100! took an instant.
TODO: It might be interesting to compute and compare the time taken by iterative and
recursive solutions.

"""
def fact(number):
 	if number > 1:
 		return number*fact(number-1)
 	else:
 		return 1

temp = str(fact(100))

answer = 0 
for digit in temp:
 	answer = answer + int(digit)
