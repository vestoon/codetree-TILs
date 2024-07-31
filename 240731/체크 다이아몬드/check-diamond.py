n = int(input())

side = n
mid = 0
for _ in range(n):
    side -= 1
    mid += 1
    print(' '*side + '* '*mid)
for _ in range(n-1):
    side += 1
    mid -= 1
    print(' '*side + '* '*mid)