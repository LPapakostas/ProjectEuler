import time

def siege_of_eratosthenes(N):
    prime = [True]*(N+1)
    p = 2
    while(p*p < N+1):
        if(prime[p] == True):
            for i in range(2*p,N+1,p):
                prime[i] = False
        p+=1
    prime[0] , prime[1] = False,False
    return prime

start = time.time() ; N = 2*10**6
primes = siege_of_eratosthenes(N)
print(sum([x for x in range(len(primes)) if primes[x]]))
print(time.time() - start,"seconds")
