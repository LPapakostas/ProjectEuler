N = 1000
lst = list(str(2**N))
print(sum( int(lst[x]) for x in range(0,len(lst))))
