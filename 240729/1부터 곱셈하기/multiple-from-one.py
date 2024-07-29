n = int(input())
acc = 1
for x in range(1, 11):
    acc *= x
    if n <= acc:
        print(x)
        break