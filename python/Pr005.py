import time
MAX = 20

# This function returns True if x is a prime number
def is_prime(x):
	if (x == 2):
		return True
	if (x<2) or (x%2 == 0) :
		return False
	for i in range(3,int(x**(0.5))+1,2):
		if (x%i == 0):
			return False
	return True
	
# Solve this problem using Least Common Multiple by Table method prime factorization
def prime_lcm():
	# Find prime numbers that included in desired range
	num = [x for x in range(1,MAX+1)]
	primes = [x for x in range(1,MAX+1) if is_prime(x)]
	ans = 1 ; pos = 0
	while (pos < len(primes)):
		index = []
		# Starting from the 1st prime number, we will keep in index list
		# the position of numbers that are evenly divided by them
		for i in range(MAX):
			if (num[i] % primes[pos] == 0):
				index.append(i)
		# While there are more than one elements that divided by <pos> prime number,
		# we divide those numbers and multiply <pos> prime number to the result
		if (len(index) >= 1):
			for j in range(len(index)):
				num[index[j]] = int(num[index[j]]/primes[pos])
			ans *= primes[pos]
		# if index list is empty, try with next prime number
		else:
			pos+=1
	return ans
	
start = time.time()
print(prime_lcm())
print("Time Evaluated : ", time.time()-start," seconds")
