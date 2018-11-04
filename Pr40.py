import time
def champ_constant(N):
    c_str= ''
    for i in range(1,N):
        c_str+=str(i)
    return c_str

start = time.time() ; N = 6 ; ans = 1
N_l = 10**N ; constant = champ_constant(N_l)
digits = set([ 10**i for i in range(N+1)])
for n in digits:
    ans*= int(constant[n-1])
print(ans,time.time()-start,"seconds")