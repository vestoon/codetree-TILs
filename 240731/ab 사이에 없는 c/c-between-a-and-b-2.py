a, b, c = map(int, input().split())
for x in range(a, b+1):
    if c%x == 0:
        print("YES")
        break
else:
    print("NO")