a_min,a_max = 2,100
b_min,b_max = 2,100
ans = []
for a in range(a_min,a_max+1):
    for b in range(b_min,b_max+1):
        if a**b not in ans:
            ans.append(a**b)
            
print(len(ans))