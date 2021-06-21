import time
N = 10000

def sum_of_gcd(x):
  s=1 # every number has 1 as a divisor
  # find divisors till sqrt of <x> because 
  # if one divisor is i, the other is x/i
  for i in range(2,int(x**0.5)+1):
    if ((x%i) == 0):
      s+=int(x/i) + i
  return s


start = time.time() ; amiable = []
# for amiable numbers, the number itselfs is not 
# included
for a in range(2,N+1):
	b = sum_of_gcd(a)
	if( a==sum_of_gcd(b) and (a!=b) and (a not in amiable)):
		amiable.append(a)
		amiable.append(b)
print(sum(amiable))
print("Time Evaluated :",time.time()-start," seconds")
