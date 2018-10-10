digits = 1000
f1,f2,index = 1,1,2
while(True):
	f1,f2,index = f2,f1+f2,index+1
	if(len(str(f2)) == digits):
		print(index)
		break