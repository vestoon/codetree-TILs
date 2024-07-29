cnt = 0
acc = 0

for _ in range(10):
    n = int(input())
    if  0<= n <= 200:
        acc += n
        cnt += 1

print(acc, f"{acc/cnt:.1f}")