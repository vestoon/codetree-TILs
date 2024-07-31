n = int(input())

blank = n -1
size = 1
for _ in range(1, n+1):
    print("  "*blank, end='')
    print("* "*size, end='')
    print()
    blank -= 1
    size += 2