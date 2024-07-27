n = int(input())
ans = 0

for _ in range(n):
    x = int(input())
    if x%2 and x%3 == 0:
        ans += x
print(ans)