

def grid20_20():
	#read data from cmd 
	L =[]
	a =[]
	for j in range(0,20):
		a= input()
		a = a.split()
		a = map(int, a)
		a = list(a)
		L.append(a)
	return L 
def grid20_horizontal(G_list):
	#multipy 4 numbers and return biggest of all 
	temp = 0 
	aux = 0
	for i in range(0,20):
		for j in range(0,16):
			aux = 1
			for k in range(0,4):
				aux *=G_list[i][j+k]
			if aux>temp:
				temp = aux 
	return temp

def grid20_right(G_list):
	#right comparison
	temp = 0  
	for i in range(0,16):
		for j in range(0,16):
			aux = 1 
			for k in range(0,4):
				aux*=G_list[i+k][j+k]
		if aux > temp:
			temp = aux 
	return aux 


def grid20_left(G_list):
	#left comparison 
	temp = 0
	for i in range(0,16):
		for j in range(0,16):
			aux = 1 
			for k in range(0,4):
				aux *= G_list[i+3-k][j+k]
			if aux > temp:
				temp = aux 
	return temp
def grid20_vert(G_list):
	#vertical comparison 
	temp = 0 
	for i in range(0,16):
		for j in range(0,20):
			aux = 1 
			for k in range(0,4):
				aux *= G_list[i+k][j]
			if aux > temp:
				temp = aux 
	return temp  			
if __name__ == "__main__":
	list =	grid20_20()
	temp1 = grid20_horizontal(list)
	temp2 = grid20_right(list)
	temp3 = grid20_left(list)
	temp4 = grid20_vert(list)
	max = [temp1,temp2,temp3,temp4]
	maxx = 0 
	for i in max:
		if i > maxx:
			maxx = i 
	print("el mayor valor es:",maxx)		
