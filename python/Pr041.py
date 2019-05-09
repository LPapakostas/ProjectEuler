import time
PERM = "123456789"

# Use of permutations of "123456789" in order to reduce 
# computation of numbers
def generate(lst):
	if (len(lst) == 1):
		return lst
	l = []
	for i in range(len(lst)):
		m = lst[i]
		rem_lst = lst[:i]+lst[i+1:]
		for x in generate(rem_lst):
			l.append(m+x)
	return l

def is_prime(n):
	x = int(n)
	for i in range(3,int(x**0.5)+1,2):
		if (x%i == 0):
			return False
	return True
	
start = time.time() ; num = []
for i in range(len(PERM)):
	num+=generate(PERM[:i+1])
num = set(num)
# remove the even numbers
num = [ x for x in num if int(x)%2 != 0 ]
primes = [ x for x in num if is_prime(x)]
print(max(primes))
print("Time Evaluated:", time.time()-start,"seconds")
