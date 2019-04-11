import time
N=20

def factorial(n):
	if n < 2:
		return 1
	else:
		return n*factorial(n-1)

start = time.time()
# We use binomical coeffiecients answer = 2N!/(N!*N!)
print(int(factorial(2*N)/(factorial(N)**2)))
print("Time Evaluated :", time.time() - start," seconds")
