import time
def pythagorian_tri(N):
    for c in range(1,N):
       for b in range(1,c):
           for a in range(1,b):
                if (a+b+c == N) and (c*c == a*a+b*b):
                    return a*b*c
    return 0

start = time.time() ; N = 1000 
print(pythagorian_tri(N),time.time()-start,"seconds")

    
