a, b = map(int, input().split())

B = b*(b+1)//2
A = a*(a-1)//2

print(B-A)