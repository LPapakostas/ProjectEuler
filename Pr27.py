import math

def isprime(num):
    s = True ; j = 2
    while(j < int(math.sqrt(num))+1):
        if( num%j == 0):
            s = False
            break
        else:
            s = True
        j+=1
    return s

def consecutive_primes(a,b):
    count = 0; n=0
    while(1):
        x = n*n+a*n+b
        if (x>0) == False :
            break
        if (isprime(x) == False) :
            break
        count+=1 ; n+=1
    return count
    
b_max = 1001 ; a_max = 1000
b_prime = []
for i in range(2,b_max):
    if (isprime(i)):
        b_prime.append(i)
        b_prime.append(-i)
        
n_max = 0 ; a_find =0 ; b_find=0
for b in b_prime:    
    for a in range(-a_max+1,a_max):
        if (a+b+1 % 2 != 0):
            num_prime = consecutive_primes(a,b)
            if(num_prime > n_max):
                n_max = num_prime
                a_find,b_find = a,b

print(a_find*b_find)