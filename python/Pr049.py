import time
UP_LIMIT = 10000 ; DOWN_LIMIT = 1487

def sieve_of_eratosthenes(N):
    prime = [True]*(N+1)
    p = 2
    while(p*p < N+1):
        if(prime[p]):
            for i in range(2*p,N+1,p):
                prime[i] = False
        p+=1
    prime[0] , prime[1] = False,False
    return prime

# Returns all permutations of s <string> to lst <list>
def permutations(s,start,stop,lst): 
    if (start == stop):
        lst.append(int(''.join(s)))
    else:
        for i in range(start,stop+1):
            s[start],s[i] = s[i],s[start]
            permutations(s,start+1,stop,lst)
            s[start],s[i] = s[i],s[start]

def check(lst):
    lst.sort()
    for i in range(len(lst)):
        for j in range(i+1,len(lst)):
            difference = lst[j] - lst[i]
            if ( lst[j] + difference in lst):
                return str(lst[i]) + str(lst[j]) + str(lst[j]+difference)
    return False

start = time.time()
# Create a list with all 4 digit primes
primes_flag = sieve_of_eratosthenes(UP_LIMIT)
primes = [x for x in range(len(primes_flag)) if primes_flag[x]]
primes_4_digits = [x for x in primes if x > DOWN_LIMIT] 
candidates = [[]]
for i in primes_4_digits:
    lst = [] ; temp = str(i)
    permutations(list(temp),0,len(temp)-1,lst)
    # with set(), we remove duplicates
    lst = list( set(lst) ) ; lst_2 = list()
    # keep only prime numbers
    for j in lst:
        if (j in primes_4_digits):
            lst_2.append(j)
    lst_2.sort() ; 
    if (lst_2 not in candidates):
        candidates.append(lst_2)
    del lst,lst_2,j
candidates.remove([]) 
for c in candidates:
    ans = check(c)
    if ( type(ans) != bool):
        print(ans)
print("Time evaluated is ", time.time()-start," s")
