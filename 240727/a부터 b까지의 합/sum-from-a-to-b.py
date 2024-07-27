a, b = map(int, input().split())

acc = 0

for x in range(a, b+1):
    acc += x

print(acc)