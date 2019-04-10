def factorial(n):
	if n < 2:
		return 1
	else:
		return n*factorial(n-1)
	
f = [int(x) for x in str(factorial(100))]	
print(sum(f[x] for x in range(0,len(f))))
