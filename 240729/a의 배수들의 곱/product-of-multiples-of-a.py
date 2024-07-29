a, b = map(int, input().split())
acc = 1
for x in range(1, b+1):
    if x%a == 0:
        acc *= x
print(acc)