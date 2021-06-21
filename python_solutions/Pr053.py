import time
LIMIT = 1000000

def factorial(n):
    if (n<2):
        return 1
    else:
        return n*factorial(n-1)

def combinations_select(n,r):
    temp = n-r 
    res = factorial(n)/(factorial(temp)*factorial(r))
    return res

start_time = time.time() 
start = 1 ; end = 100 ; count = 0
for i in range(start,end+1):
    for j in range(start,i):
        if (combinations_select(i,j) > LIMIT):
            count+=1
print(count)
print("Time evaluated : ", time.time()-start_time," s")