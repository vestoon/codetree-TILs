n = int(input())
acc = 0
for x in range(1, 101):
    acc += x
    if acc >= n:
        print(x)
        break