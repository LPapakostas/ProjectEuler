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

N = 10001
nofprime = 1
i = 2
while(1):
    i+=1
    if(isprime(i)):
        nofprime+=1
    if(nofprime == N):
        print(i)
        break
