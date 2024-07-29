n = int(input())
acc = 0
for x in range(1, n):
    if not n%x:
        acc += x

print('P' if acc == n else 'N')