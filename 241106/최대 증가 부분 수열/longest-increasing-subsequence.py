import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

dp = [1 for x in range(N)]
dp[0] = 1
for j in range(1, N):
    for i in range(j):
        if arr[i] < arr[j]:
            dp[j] = max(dp[j], dp[i]+1)

print(max(dp))