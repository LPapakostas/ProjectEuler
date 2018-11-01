coins = set([1,2,5,10,20,50,100,200])
N = 200 
combinations = [0]*(N+1) ; combinations[0] = 1
for c in coins:
    for i in range(len(combinations)):
        if ( i >= c):
            combinations[i]+=combinations[i-c]
print(combinations[-1])