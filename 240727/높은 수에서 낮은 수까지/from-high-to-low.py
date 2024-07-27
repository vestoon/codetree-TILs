a, b = map(int ,input().split())

print(*[x for x in range(max(a, b), min(a, b)-1, -1)])