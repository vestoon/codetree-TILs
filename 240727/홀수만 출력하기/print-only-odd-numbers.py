import sys
input = sys.stdin.readline

n = int(input())
for _ in range(n):
    x = int(input())
    if x%2 and x%3 == 0:
        print(x)