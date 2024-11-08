import sys
input = sys.stdin.readline

"""
3xn 차원 dp? 
"""

n = int(input())
stairs = list(map(int, input().split()))
dp = [[0 for x in range(n)] for _ in range(4)]
dp[0][1] = stairs[1]
dp[1][0] = stairs[0]

#dp[i][j] = 1칸씩 올라가는 연산을 i 번 한 상태로  j-1층까지 올라갔을 때 얻을 수 있는 동전의 최대값

for j in range(n-1):
    for i in range(4): # dp[i][j+2], dp[i+1][j+1] 을 갱신
        if not dp[i][j]: continue
        if j != n-2:
                dp[i][j+2] = max(dp[i][j+2], dp[i][j] + stairs[j+2])
        if i != 3:
            dp[i+1][j+1] = max(dp[i+1][j+1], dp[i][j]+stairs[j+1])
    
# for _ in dp:
#     print(*_)
print(max(dp[0][n-1], dp[1][n-1], dp[2][n-1], dp[3][n-1]))
# print(dp[0][n-1], dp[1][n-1], dp[2][n-1], dp[3][n-1])