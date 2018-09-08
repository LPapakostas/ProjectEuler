import math

ans = 1
for i in range(1,21):
    ans = int(ans*i/math.gcd(i,ans))
print(ans)
