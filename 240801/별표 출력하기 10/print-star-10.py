n = int(input())
for x in range(2*n):
    cnt = n-(x-1)//2 if x%2 else 1+(x//2)
    print('* '*cnt)