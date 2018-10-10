from fractions import gcd
import math

def amiable(k):
	s=1
	for i in range(2,int(math.sqrt(k))):
		temp = gcd(k,i)
		if (temp!=1):
			s+=temp
	return s
	

N = 10000
lst = []
for a in range(2,N+1):
	b = amiable(a)
	if( a==amiable(b) and (a!=b) and (a not in lst) and (b not in lst)):
		lst.append(a)
		lst.append(b)
print(sum(lst))