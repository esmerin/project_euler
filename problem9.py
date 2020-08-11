#import pitagoras from euler 
import math 
def bol_triple(a,b,c):
	if ((a*a + b*b) == c*c):
		return True
	else:
		return False 
def solucion():
	for i in range(1,1000):
		for j in range(1000,1,-1):
			k = 1000-i-j
			if(k > i and k >j):
				if( bol_triple(i,j,k)):
					return i*j*k			 
if __name__ == "__main__":
	print(solucion())
