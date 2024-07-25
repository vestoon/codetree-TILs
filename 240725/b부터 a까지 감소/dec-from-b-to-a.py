a, b = map(int, input().split())
print(*[x for x in range(b, a-1, -1)])