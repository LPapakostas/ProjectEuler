import math
def up_lim():
    d = 1 
    while(True):
        if(d-math.log(d,10)+1 >= 5.77):
            break
        d+=1
    return d*(9**5)

def is_fifth_sum(x,fifth_power):
    num = x ; sum_pow = 0
    while(x!=0):
        sum_pow += fifth_power[x%10]
        x=int(x/10)
    if(sum_pow == num):
        return True
    return False
      
lim = up_lim()
pow5 = [x**5 for x in range(0,10)]
print(sum([x for x in range(4,lim+1) if( is_fifth_sum(x,pow5) )]))
