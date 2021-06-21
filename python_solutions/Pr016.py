import time
N = 1000

start = time.time()
lst = list(str(2**N))
print(sum( int(lst[x]) for x in range(0,len(lst))))
print("Time Evaluated :", time.time()-start," seconds")
