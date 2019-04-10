def collage_series(n):
    num = 1
    while(n != 1):
        if(n%2 == 0):
            n=n/2
        else:
            n=3*n+1
        num+=1
    return num

N = 1000000
max_chain_number = 0
max_chain = 0
for i in range(1,N+1):
    if(collage_series(i) >= max_chain):
        (max_chain , max_chain_number) = (collage_series(i),i)

print(max_chain_number)
