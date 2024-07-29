n = int(input())
tmp = n
for x in range(1, n+1):
    tmp //= x
    if not tmp:
        print(x)
        break