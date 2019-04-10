import math

def sum_of_gcd(x):
  s=1
  for i in range(2,int(math.sqrt(x))+1):
    if ((x%i) == 0):
      s+=x/i + i
  return int(s)

N = 10000
lst = []
for a in range(2,N+1):
	b = sum_of_gcd(a)
	if( a==sum_of_gcd(b) and (a!=b) and (a not in lst)):
		lst.append(a)
		lst.append(b)
print(sum(lst))
