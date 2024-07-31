n = int(input())
for x in range(n, 0, -1):
    for _ in range(x):
        print('*'*x, end=' ')
    print()