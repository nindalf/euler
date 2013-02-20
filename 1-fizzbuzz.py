#! /usr/bin/env python3
"""
Although this problem appears deceptively easy, Jeff Atwood of Stackoverflow claims
that most programmers are unable to solve this.
http://www.codinghorror.com/blog/2007/02/why-cant-programmers-program.html

"""
answer = 0
for i in range(3, 1001):
	if i%3 == 0 or i%5 == 0:
		answer = answer + i 
		
print(answer)
