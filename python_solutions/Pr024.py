'''
We use Lehmer code to solve this problem
http://math.shaunlgs.com/lehmer-code/
'''

def factorial(n):
    if n < 2:
        return 1
    else:
        return n*factorial(n-1)
    
def to_lehmer(x,factors):
    num = []
    for i in range(len(factors)):
        num.append(int(x/factors[i]))
        x -= int(x/factors[i])*factors[i]
    return num

def max_count(count,lst):
    for i in range(len(lst)):
        c = 0 ; x=lst[i]
        for j in lst:
            if x > j:
                c+=1
        if (c == count):
            return x,i

def lehmer_to_perm(a,digits):
    perm = [int(x) for x in digits]
    for i in range(len(perm)):
        temp = perm[i:]
        x,pos = max_count(a[i],temp)
        perm[i] , perm[i+pos] = x , perm[i]
    return perm

digits = list("0123456789")
N = 1000000
factor =[]
for i in range(int(max(digits))+1):
    factor.append(factorial(i))
factor = factor[::-1]
lem_num = to_lehmer(N-1,factor) #list
ans = lehmer_to_perm(lem_num,digits)
print(''.join(str(x) for x in ans))


