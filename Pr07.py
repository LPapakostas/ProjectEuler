import math , time

def isprime(num):
    s = 1 ; j = 2
    while(j<=round(math.sqrt(num))):
        if( num%j == 0):
            s = 0
            break
        j+=1
    return s

start_time = time.time()
N = 10001 ; nofprime = 1 ; i = 2
while(True):
    i+=1
    if isprime(i) :
        nofprime+=1
    if(nofprime == N):
        break
print(i,time.time() - start_time,"seconds")
