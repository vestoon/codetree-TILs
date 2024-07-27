n = int(input())

for x in range(1, n+1):
    if x%2 == 0 or x%3 == 0:
        print(1, end = ' ' )
    else:
        print(0, end=' ')