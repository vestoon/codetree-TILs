cnt = 0
for _ in range(3):
    a, b = input().split()
    if a == 'Y' and int(b) >= 37:
        cnt += 1

print('E' if cnt >= 2 else 'N')