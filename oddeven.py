def evenOdd(n):
	if(n % 2 == 0):
		return True

	elif(n %2 != 0):
		return False

n=int(input())
if(evenOdd( n )):
	print("num is even")
else:
	print("num is odd")
