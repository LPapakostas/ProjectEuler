import time
N = 10001

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


start = time.time()
# We start from 3 in order to increase our step by 2 
n_of_prime = 2 ; num = 3
while (n_of_prime < N):
	num+=2
	if is_prime(num):
		n_of_prime +=1
	
print(num) ; print("Time Evaluated :", time.time() - start, "seconds")
