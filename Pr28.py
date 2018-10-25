N = 1001 
print(sum([4*i*i-6*(i-1) for i in range(3,N+1,2)])+1)
'''
up_right = i*i
uP_left = i*i - (i-1)
down_right = i*i - 3*(i-1)
down_left = i*i - 2*(i-1)
'''   
    