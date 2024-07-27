a, b = map(int, input().split())
acc = 0
cnt = 0
for x in range(a, b+1):
    if x%5 == 0 or x%7 == 0:
        acc += x
        cnt += 1

print(acc, f"{acc/cnt:.1f}")