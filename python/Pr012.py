import time
N = 500

def sum_of_gcd(num):
    dividers = 2 # 1 and <num> itselfs as a factor
    for i in range(2,int(num**(0.5))+1):
        if( num%i == 0):
            dividers+=2 # d and n/d factors
    return dividers # the number itself as a factor

start = time.time()
triag = 1 ; i = 1
while(sum_of_gcd(triag) < N+1):
	i+=1 ; triag+=i
print(triag)
print("Time Evaluated: ", time.time() - start, "seconds") 
