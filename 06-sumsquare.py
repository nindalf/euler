#! /usr/bin/env python3
"""
Done with minimal effort. The method of creating the required list is known as
list comprehensions.

"""

limit = 100

squares = [i*i for i in range(1, limit+1)]
sumsquares = sum(squares)

sequence = [i for i in range(1, limit+1)]
sumseq = sum(sequence)

print(sumsquares - sumseq*sumseq)
