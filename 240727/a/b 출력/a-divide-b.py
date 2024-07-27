a, b = map(int, input().split())

d = a//b
r = a%b
print(d, '.', end='',sep='')

for _ in range(20):
    r *= 10
    q = r//b
    r = r%b
    print(q,end='')