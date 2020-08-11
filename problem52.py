"""
It can be seen that the number, 125874, and its double, 251748,
 contain exactly the same digits, but in a different order.
Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.
"""
def digits(n):
#return the digits of n in a list 
	aux = []
	while(n>0):
		aux.append(n%10)
		n =int(n/10)
	return aux 
# elem in list 
def bol_same_digit(n1,n2):
	#compare if bot have the same digit 
	list1 = digits(n1)
	list2 = digits(n2) 
	if (not(len(list1) == len(list2))):
		return False
	for i in list1:
		if(not(i in list2)):
			return False
		list2.remove(i) 
	return True 
#print(bol_same_digit(12345,23145),bol_same_digit(111,222))
def solucion():
	s = False
	n = 1
	while(not s):
		if (bol_same_digit(n,2*n)):
			if(bol_same_digit(n,3*n)):
				if(bol_same_digit(n,4*n)):
					if(bol_same_digit(n,5*n)):
						if(bol_same_digit(n,6*n)):
							return n
		n += 1
		if(n > 1000000000):
			print("no lo se rick")
			return 0
	
#print(bol_same_digit(99,99*6))
print(solucion())
