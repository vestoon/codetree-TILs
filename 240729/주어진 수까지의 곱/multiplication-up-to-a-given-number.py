a, b = map(int, input().split())
acc = 1

for x in range(a, b+1):
    acc *= x

print(acc)