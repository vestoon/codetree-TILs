a,b  = map(int, input().split())
acc = 0
for x in range(a, b+1):
    if x%6 == 0 and x%8:
        acc += x
    
print(acc)