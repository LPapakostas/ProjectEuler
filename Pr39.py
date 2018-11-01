import time
def tri_comb(x):
    count = 0
    for a in range(1,x):
        # solve the following system for b
        # a^2 + b^2 = c^2 (1)
        # a+b+c = x (2)
        b = int((x*x - 2*a*x)/(2*x-2*a))
        c = x-a-b 
        if (c > b > a) and (a+b+c == x) and (a*a+b*b == c*c):
            count+=1 
    return count

start = time.time()
N = 1000 ; max_perimeter = 3 ; max_c = 1
p = set([x for x in range(3,N+1)])
for n in p:
    temp = tri_comb(n)
    if (temp >= max_c):
        max_perimeter,max_c = n,temp
print(max_perimeter,"Time:",time.time()-start,"seconds")