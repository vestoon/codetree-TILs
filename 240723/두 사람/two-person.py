for _ in range(2):
    a, g = map(int, input().split())
    if a >=19 and g=='M':
        print(1)
        break
else:
    print(0)