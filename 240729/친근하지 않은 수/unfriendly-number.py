n = int(input())
cnt = 0

for x in range(1, n+1):
    if x%2 and x%5 and x%3:
        cnt += 1
print(cnt)