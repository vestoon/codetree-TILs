n = int(input())

for x in range(2, n):
    if n%x == 0:
        print('C')
        break
else:
    print('P')