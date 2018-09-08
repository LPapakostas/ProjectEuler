import math

def sum_of_gcd(num):
    s = 1 # 1 as a factor
    for i in range(2,round(math.sqrt(num))):
        if( num%i == 0):
            s+=2 # d and n/d factors
    return s+1 # the number itself as a factor

N = 500
triag = 1
i = 1
while(1):
    if(sum_of_gcd(triag)> N):
        print(triag)
        break
    i+=1
    triag+=i
