import time
global limit

def condition(n,d):
    # digits(n_k)>digits(d_k)
    if ( len(str(n)) - len(str(d)) == 1 ):
        return True
    return False 

start_time = time.time()
limit = 1000
# n_k+1 = n_k + d_k
# d_k+1 = n_k + 2*d_k
n_k = 3 ; d_k = 2 ; count = 0
for i in range(1,limit+1):
    if condition(n_k,d_k) :
        count+=1
    d_k,n_k = d_k + n_k ,n_k + 2*d_k
print(count)
print("Time evaluated in seconds",time.time()-start_time," s")