import time
LIMIT = 100
start = time.time();sums_pow = []
for a in range(LIMIT):
    for b in range(LIMIT):
        ans = sum(int(x) for x in str(a**b))
        sums_pow.append(ans)
print(max(sums_pow))
print("Time evaluated ",time.time()-start," s")