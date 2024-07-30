import math

n = int(input())
m = math.ceil(math.sqrt(n))

for x in range(2, m+1):
    if n%x == 0:
        print('C')
        break
else:
    print('N')