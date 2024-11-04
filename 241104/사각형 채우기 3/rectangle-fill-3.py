n = int(input())
mod = 1000000007

# 윗줄의 길이가 i 이고 아랫줄의 길이가j 일 때 의 가짓수
dp = [[0 for x in range(max(3, n+1))] for y in range(max(3, n+1))]
dp[1][0] = 1
dp[0][1] = 1
dp[1][2] = 3
dp[2][1] = 3
dp[1][1] = 2
dp[2][2] = 7

for i in range(3, n+1):
    dp[i][i] += dp[i-2][i-2] +dp[i-1][i-2] + dp[i-2][i-1] + 2*dp[i-1][i-1]
    dp[i][i] %= mod

    dp[i][i-1] += dp[i-1][i-1] + dp[i-1][i-2]
    dp[i-1][i] += dp[i-1][i-1] + dp[i-2][i-1]
    dp[i][i-1] %= mod
    dp[i-1][i] %= mod
    # dp[i-1][i-1] += dp[i-2][i-2]

print(dp[n][n])