import time
def is_palidrome_dec(x):
    if (str(x) == str(x)[::-1]):
        return True
def is_palindrome_bin(x):
    xb = bin(x)[2:]
    if (xb == xb[::-1]):
        return int(x)
    return 0
    
N = 10**6; num = [False]*N ; start = time.time()
for i in range(1,N):
    num[i-1] = is_palidrome_dec(i)
palidrome_dec = set([(x+1) for x in range(len(num)) if num[x] ])
ans = 0
for n in palidrome_dec:
    ans+=is_palindrome_bin(n)
print(ans,"Time:",time.time()-start,"seconds")