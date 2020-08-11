import math 
#we need two functions so one do the square of the route and the other the root of the square

def sum_of_square(n):
	total = 0 
	for i in range(1,n+1):
		total += math.pow(i,2)
	return total 
def square_of_sum(n):
	total = 0 
	"""
	for i in range(1,n+1):
		total += i 
	total = math.pow(total,2)
	"""
	total = (n*(n+1))/2
	total = math.pow(total,2)
	return total 
def solution():
	n1 = sum_of_square(100)
	n2 = square_of_sum(100)
	return n2 - n1 

if __name__ == "__main__":
	print(solution())
