import numpy as np

def product(x,y,dx,dy,n,a):
  pr=1
  for i in range(n):
    pr*=a[x+i*dx,y+i*dy]
  return pr

a = np.loadtxt("Pr11_numbers.txt",dtype = int)
n,p = a.shape
ans = -1
N = 4
for i in range(n):
  for j in range(p):
    up,down,left,right = (-1 <i-3),(i+3 < n),(-1 < j-3),(j+3 < p)
  
    if up:
      ans = max(product(i,j,-1,0,N,a),ans)
    if down:
      ans = max(product(i,j,1,0,N,a),ans)
    if left:
      ans = max(product(i,j,0,-1,N,a),ans)
    if right:
      ans = max(product(i,j,0,1,N,a),ans)
    if (down and right):
      ans = max(product(i,j,1,1,N,a),ans)
    if (up and left):
      ans = max(product(i,j,-1,-1,N,a),ans)
    if (up and right):
      ans = max(product(i,j,-1,1,N,a),ans)
    if (down and left):
      ans = max(product(i,j,1,-1,N,a),ans)

print(ans)

