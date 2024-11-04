import sys
input = sys.stdin.readline

N = int(input())
grid = [list(map(int, input().split())) for x in range(N)]

dp = [[0 for x in range(N)] for y in range(N)]
dp[0][0] = grid[0][0]

for j in range(1, N):
    dp[0][j] = grid[0][j] + dp[0][j-1]
for i in range(1, N):
    dp[i][0] = grid[i][0] + dp[i-1][0]

for i in range(1, N):
    for j in range(1, N):
        dp[i][j] = grid[i][j] + max(dp[i-1][j], dp[i][j-1])

print(dp[N-1][N-1])