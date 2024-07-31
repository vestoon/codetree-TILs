n = int(input())

side = n
mid = 0
for _ in range(n):
    print('*'*side + ' '*mid + '*'*side)
    side -= 1
    mid += 2