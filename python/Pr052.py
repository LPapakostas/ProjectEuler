import time
LIMIT = 9876543210

def isPerm(num1,num2):
    num2_sep = [] ; pows = len(str(num2))
    # Separate num in its distinct digits
    divisor = num2 ; rem = 0
    for i in range(pows-1,0,-1):
        temp = int(divisor/(10**i)) ; num2_sep.append(str(temp))
        rem = divisor%(10**i)
        if len(str(rem)) == 1:
            num2_sep.append(str(rem))
            break
        divisor = rem
    # Check if those numbers have same digits
    num2_sep.sort(); n2_check = ''.join(num2_sep)
    num1_list = list(str(num1)) ; num1_list.sort() ; n1_check = ''.join(num1_list)
    if (n1_check == n2_check):
        return True
    return False
    
def check(i):
    multiples = [2,3,4,5,6] ; num = [x*i for x in multiples]
    s_i = str(i) ; perm_lst=[] ; flag = 0
    for n in num:
        if (isPerm(i,n)):
            flag+=1
    if (flag < len(num)-1):
        return False
    return True

start = time.time() ; count = 100000 ; flag = False
x1 = 125874 ; x2 = 251748
while(count < LIMIT):
    flag = check(count)
    if flag :
        print(count); break
    count+=1
print("Time evaluated is ", time.time()-start,"s")