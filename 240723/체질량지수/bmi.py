h, w = map(int, input().split())

b = w*10000//(h*h)
print(b)
if b >= 25:
    print("Obesity")