c, n = input().split()
n = int(n)
if c == 'A':
    print(*[x for x in range(1, n+1)])
else:
    print(*[x for x in range(n, 0, -1)])