a = int(input())
for x in range(1, a+1):
    if (x%2 or x%4==0) and (x//8)%2 and (x%7>=4):
        print(x, end=' ')