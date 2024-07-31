n = int(input())

side = 0
mid = 2*n - 1
for _ in range(n):
    print('  '*side + '* '*mid)
    side += 1
    mid -= 2

side -= 1
mid += 2
for _ in range(n-1):
    side -= 1
    mid += 2
    print('  '*side + '* '*mid)