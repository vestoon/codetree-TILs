a, b = map(int, input().split())
for x in range(a, b+1):
    if 1920%x == 0 and 2880%x == 0:
        print(1)
        break
else:
    print(0)