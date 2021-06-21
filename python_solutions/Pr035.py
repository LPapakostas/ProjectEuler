import math , time
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

def is_circular_prime(prime_num):
    circ=[]
    for n in prime_num:
        temp = [n]
        circle = len(str(n))
        if (circle == 1):
            circ.append(n)
        else:
            div = 10**(circle-1)
            for i in range(1,circle):
                n = int(str(int(n%div))+str(int(n/div)))
                if (n in prime_num) :
                    temp.append(n)
                else:
                    break
            if(len(temp) == circle):
                for j in range(len(temp)):
                    if temp[j] not in circ:
                        circ.append(temp[j])
    return circ

N = 10**6 ; start = time.time()
primes = siege_of_eratosthenes(N)
prime_num = set([x for x in range(len(primes)) if primes[x]])
print(len(prime_num))
c = is_circular_prime(prime_num)
print(len(c),"Time",time.time()-start,"seconds")
    