n = int(input())
n = 2*n - 1
blank = 0

while n >= 1:
    print("  "*blank, end='')
    print("* "*n, end='')
    print()
    n -= 2
    blank += 1