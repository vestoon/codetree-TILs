n = int(input())

cnt = 0
while n < 1000:
    cnt += 1
    if n%2:
        n = n*2 + 2
    else:
        n = n*3 + 1

print(cnt)