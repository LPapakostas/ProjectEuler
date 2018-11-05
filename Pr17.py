import time
one_to_nin = ["one","two","three","four","five","six","seven","eight","nine","ten",
              "eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen",
            "eighteen","nineteen"]
tens = ["twenty","thirty","forty","fifty","sixty","seventy","eighty","ninety"]
a = "and" ; h = "hundred"

def letters_of_num(i):
    ans = 0
    if (len(str(i)) == 2):
        un = int(i%10) ; dec = int(i/10)
        if (un == 0):
            ans = len(tens[dec-2])
        else:
            ans = (len(tens[dec-2]) + len(one_to_nin[un-1]))
    else:
        hun = int(i/100) ; res = int(i%100)
        if (res == 0):
            ans = (len(one_to_nin[hun-1]) + len(h))
        elif (res>=1) and (res<=19) :
            ans = (len(one_to_nin[hun-1]) + len(h) + len(a) + len(one_to_nin[res-1]))
        else:
            dec = int(res/10) ; un = int(res%10)
            if(un != 0):
                ans = (len(one_to_nin[hun-1]) + len(h) + len(a) + len(tens[dec-2]) + len(one_to_nin[un-1]))
            else:
                ans = (len(one_to_nin[hun-1]) + len(h) + len(a) + len(tens[dec-2]))
    return ans
  
start = time.time() ; N = 1000 ; ans = 0 
ans += sum([len(x) for x in one_to_nin])
for i in range(20,N):
    ans += letters_of_num(i)
print(ans+len('onethousand'),time.time()-start,"seconds")
        
    