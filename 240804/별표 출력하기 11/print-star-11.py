n = int(input())
border = '* '*(2*n+1)
inner = '*   '*n + '*'

for _ in range(n):
    print(border)
    print(inner)
print(border)