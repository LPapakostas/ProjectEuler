import time
LIMIT = 10000; LIMIT_ITER = 50

def is_palindrome(num):
    assert type(num) is str
    if(num == num[::-1]):
        return True
    return False

def is_lychrel(num):
    for i in range(1,LIMIT_ITER):
        num+= int( (str(num)[::-1]) )
        if (is_palindrome(str(num))):
            return False
    return True

start = time.time() ; count =0 
for i in range(1,LIMIT):
    if is_lychrel(i):  count+=1 
print(count)
print("Time evaluate :",time.time()-start," s" )