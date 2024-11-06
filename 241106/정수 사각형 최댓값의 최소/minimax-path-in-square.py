import sys
input = sys.stdin.readline

n = int(input())
grid = [list(map(int, input().split())) for y in  range(n)]


"""
dp[i][j] = i, j 까지 왔을 때거쳐갈 수 있는 최대값?
0, 0 에서 i, j까지 가는 길이 3 가지 있다고 하자
세 루트에서의 각각 최대값은 3가지 이고 이중 최소값을 저장한다. 

"""

dp = [[0 for x in range(n)] for y in range(n)]
dp[0][0] = grid[0][0]

for i in range(1, n):
    dp[i][0] = max(dp[i-1][0], grid[i][0])

for j in range(1, n):
    dp[0][j] = max(dp[0][j-1], grid[0][j])

for i in range(1, n):
    for j in range(1, n):
        dp[i][j] = min(max(dp[i-1][j], grid[i][j]), max(dp[i][j-1], grid[i][j]))

print(dp[n-1][n-1])