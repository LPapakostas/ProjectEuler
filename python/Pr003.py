import time
start_time = time.time()
N = 600851475143 ; p = 2
# Starting by 2 , we will divide each time the p number
# doing prime factorization
while (N >= p*p):
    if ( N%p == 0):
        N = N/p
    else:
        p+=1
print(N)
print(time.time() - start_time,"seconds")
    
