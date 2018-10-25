def repeatable(num):
    x = 10 ; rep_count = 0
    while(rep_count<1) or (x!=10) :
        x = (x%num)*10
        rep_count+=1
    return rep_count
   
N = 1000
max_num = 1 ; max_proc = 0
for i in range(2,N):
    if(i%2 != 0) and (i%5 != 0):
        temp = repeatable(i)
        if( temp> max_proc):
            max_num,max_proc = i,temp      
print(max_num)