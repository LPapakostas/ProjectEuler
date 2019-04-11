import time
N = 100

def factorial(n):
	if n < 2:
		return 1
	else:
		return n*factorial(n-1)

start = time.time()
# <f> list contains all of digitis of N!
f = [int(x) for x in str(factorial(N))]	
print(sum(f[i] for i in range(len(f))))
print("Time Evaluated :",time.time()-start," seconds")
