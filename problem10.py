import euler
number_of_prime = 140579
list = [] 
list = euler.prime_list(number_of_prime)
total = 0
for primo in list:
	if(primo < 2000000):
		total += primo
	else:
		break
print(total)
