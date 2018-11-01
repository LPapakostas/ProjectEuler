import math,time
start_time = time.time()

(f0,f1) = (1,1)
ans = 0 ; N = 4000000
while (f1 < N):
    if ( f1%2 == 0):
        ans+=f1
    (f0,f1) = (f1,f1+f0)    
print(ans)
print(time.time() - start_time,"seconds")
