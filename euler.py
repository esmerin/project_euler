#this is a module that has all important function for the challenge 

#for problem 7
def prime_list(limit):
	len_list = 1 
	prime_list = [2]
	n = 3
	bol_prime = True
	while (len_list <= limit):
		for prime in prime_list:
			if(n%prime == 0):
				bol_prime = False 	
				break	
		if (bol_prime == True):
			prime_list.append(n)
			print(len_list)
			len_list += 1
			n += 1
		else:
			bol_prime = True 
			n += 1
	#print(n,len_list)
	return prime_list 
#print(prime_list(10))
def pitagoras(a,b):
	return a*a + b*b 
