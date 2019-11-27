import time
LIMIT = 1000000

def sieve_of_eratosthenes(N):
    prime = [True]*(N+1)
    p = 2
    while(p*p < N+1):
        if(prime[p]):
            for i in range(2*p,N+1,p):
                prime[i] = False
        p+=1
    prime[0],prime[1] = False,False
    return prime

def sum_limit(primes):
    sums = [primes[0]] 
    for i in range(1,len(primes)):
        temp = sums[-1]+primes[i]
        if (temp > LIMIT):
            return len(sums)
        sums.append(temp)
    return len(sums)

# Create a dictionary with primes 
start = time.time()
p_flag = sieve_of_eratosthenes(LIMIT)
primes = [x for x in range(len(p_flag)) if p_flag[x]]
# Find primes limit for summaries that exceed LIMIT
end_j = sum_limit(primes) 
length_chain = 0 ; val = 0 
for i in range(len(primes)):
    for j in range(i+length_chain,end_j+1):
        ans = sum(primes[i:j]) ; 
        if (ans in primes):
            length_chain = j-i ; val=ans ; lst = primes[i:j]

print(length_chain,val)
print("Time evaluated : ", time.time() - start," s")