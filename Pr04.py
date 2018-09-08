import math

def maximum(p,m):
    if p > m:
        return p
    else:
        return m
    
max_pali = int(1)
for i in range(100,1000):
    for j in range(100,1000):
        if (str(i*j) == str(i*j)[::-1]):
            max_pali = maximum(i*j,max_pali)
            
print(max_pali)
