import math

def isprime(num):
    s = 1
    j = 2
    while(j<=math.ceil(math.sqrt(num))):
        if( num%j == 0):
            s = 0
            break
        else:
            s = 1
        j+=1
    return s

ans = sum(x for x in range(3,2000000,2) if( isprime(x)==1 ) ) 
print(ans+2)
