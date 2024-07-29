import sys
input = sys.stdin.readline

n = int(input())
acc = 0

for _ in range(n):
    acc += int(input())

print(acc, f"{acc/n:.1f}")