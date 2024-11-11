import sys
input = sys.stdin.readline

"""
n 층으로 이루어진 신전, 층마다 방 3개 하나만 갈 수 있음

직전 층에서 들어간 방 중복으로 가기 불가능

꼭대기와 1층의 방의 종류가 같으면 안된다. 

dp[i][j][k] : [i] 1층에서 선택한 방의 종류 [j] 현재 층 수 [k] 현재 층으 방 종류
"""

n = int(input())
dp = [[[0 for x in range(3)] for y in range(n)] for z in range(3)]
temple = []

for _ in range(n):
    l, m, r = map(int, input().split())
    temple.append((l, m, r))

for i in range(3): # 1 층에서 i 종류의 방을 선택했을 때 
    dp[i][0][i] = temple[0][i]
    
    for j in range(1, n):
        for k in range(3): # 현재 선택한 방의 종류
            for pk in range(3): # 이전에 선택한 방의 종류
                if k == pk: continue

                dp[i][j][k] = max(dp[i][j][k], dp[i][j-1][pk]+temple[j][k])

print(max(max(dp[0][n-1][1], dp[0][n-1][2]), max(dp[1][n-1][0], dp[1][n-1][2]), max(dp[2][n-1][0], dp[2][n-1][1])))