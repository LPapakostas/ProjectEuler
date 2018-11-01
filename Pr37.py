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

def is_trunc(x,prime_num):
    dig = len(str(x)) ; primes=1
    if (dig == 1):
        return False
    for i in range(1,dig):
        if int(str(x)[i:]) in prime_num:
            primes+=1
        else:
            break
    for i in range(dig-1,0,-1):
        if int(str(x)[:i]) in prime_num:
            primes+=1
        else:
            break
    if (primes == 2*dig-1):
        return True
    return False

start = time.time()
N = 10**6 ; p = siege_of_eratosthenes(N) ; trunc=[]
prime_num =set([x for x in range(len(p)) if p[x]])
for n in prime_num:
    if is_trunc(n,prime_num):
        trunc.append(n)
if (len(trunc) == 11):
    print(sum(trunc) , "Time",time.time()-start,"seconds")
else:
    print("More")