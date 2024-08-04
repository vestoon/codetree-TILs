n = int(input())

i, j = n, 1

for _ in range(n):
    print('* '*i)
    print('* '*j)

    i -= 1
    j += 1