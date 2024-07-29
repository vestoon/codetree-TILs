n = int(input())
tmp = n
for x in range(1, n+1):
    tmp //= x
    if tmp <= 1:
        print(x)
        break
else:
    print(x)