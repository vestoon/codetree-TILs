n = int(input())

blank = n
cnt = 0

for _ in range(n):
    blank -= 1
    cnt += 1
    print('  '*blank + '@ '*cnt)
for _ in range(n-1):
    blank += 1
    cnt -= 1
    print('@ '*cnt + '  '*blank)