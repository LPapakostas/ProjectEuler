import math

N = 600851475143
p = 2
while (N >= p*p):
    if ( N%p == 0):
        N = N/p;
    else:
        p+=1
print(N)
    
