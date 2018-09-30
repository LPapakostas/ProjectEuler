def factorial(n):
	if n < 2:
		return 1
	else:
		return n*factorial(n-1)
	

num = factorial(100)
f = [int(x) for x in str(num)]	
ans = sum([f[x] for x in range(0,len(f))])
print(ans)