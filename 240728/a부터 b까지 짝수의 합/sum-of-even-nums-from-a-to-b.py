a, b = map(int, input().split())

acc = 0
for x in range(a, b+1): 
    if x%2 == 0:
        acc += x
print(acc)