n = int(input())

if n%2 and not n%3:
    print("true")
elif n%2 == 0 and n%5 == 0:
    print("true")
else:
    print("false")