n = int(input())
for i in range(1, n+1):
    s =str(i)
    if i%3 == 0 or '3' in s or '6' in s or '9' in s:
        print(0, end=' ')
    else:
        print(i, end=' ')