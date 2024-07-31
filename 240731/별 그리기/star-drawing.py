n = int(input())

side = n
mid = -1
for _ in range(n):
    side -= 1
    mid += 2
    print(' '*side + '*'*mid)

for _ in range(n-1):
    side += 1
    mid -= 2
    print(' '*side + '*'*mid)