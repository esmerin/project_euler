"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""
import math
def divisors(n):
	list = []
	for i in range(2,int(math.sqrt(n))):
		if(n%i == 0):
			list.append(i)
	return list 
#print(divisors(2520))	
