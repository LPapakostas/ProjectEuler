import math
def is_abundant(x):
    s=1
    #int(math.sqrt(x)
    for i in range(2,int(x/2)+1):
        if ( x%i == 0 ):
            s+=i
    if x < s:
        return True
    return False

N = 28124
abundants = [ x for x in range(1,N) if is_abundant(x)]
sum_2_ab= [False]*N
for i in range(len(abundants)):
  for j in range(i,len(abundants)):
    temp = (abundants[i]+abundants[j])
    if(temp < N):
      sum_2_ab[temp] = True
    else:
        break

print(sum(i for i in range(len(sum_2_ab)) if not sum_2_ab[i]))