n = int(input())
for x in range(1, n+1):
    if x%2 and x%10 != 5 and (x%3 or x%9 == 0):
        print(x, end=' ')