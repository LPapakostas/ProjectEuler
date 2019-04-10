import time
def maximum(p,m):
    if p > m:
        return p
    return m

start = time.time()
max_pali = 1 ; start_val = 100 ; stop_val = 1000
for i in range(start_val,stop_val):
    for j in range(start_val,stop_val):
        if (str(i*j) == str(i*j)[::-1]):
            max_pali = maximum(i*j,max_pali)

print(max_pali,time.time()-start,"seconds")
