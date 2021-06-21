import time
start_value = 9 
primes = set([2,3,5,7])

def is_prime(num):
	if num == 2:
		return True
	else:
		for i in range(3,int(num**0.5)+1,2):
			if (num%i == 0):
				return False
		return True

start = time.time() ; ans = 0
i = start_value ; flag = True
while(flag):
	if (is_prime(i)):
		primes.add(i)
	else:
		ans = i ; p_logic = set()
		# x = p + 2*j^2 => j = ((x-p)**0.5)/2
		for j in range(1,int((i/2)**0.5)+1):
			p = i - 2*(j**2)
			p_logic.add(p in primes)
		flag = any(p_logic)
	i+=2
print(ans)
print("Time Evaluated:", time.time()-start,"seconds") 
