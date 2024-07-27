a, b = map(int, input().split())
if b < a:
    a, b = b, a

acc = 0
for x in range(a, b+1):
    if x%5 == 0:
        acc += x
print(acc)