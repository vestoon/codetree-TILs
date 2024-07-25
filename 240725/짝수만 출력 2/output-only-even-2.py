a, b = map(int, input().split())
for x in range(a, b-1, -1):
    if not x%2:
        print(x, end=' ')