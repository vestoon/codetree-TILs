import sys
n = int(input())
chessBoard = [list(map(int, input().split())) for x in range(n)]
visited = [False for x in range(n)] # 각 열들의 방문 상태
cur_sum = 0
max_sum = 0


def findMax(cur):
    global cur_sum, max_sum
    if cur == n:
        max_sum = max(max_sum, cur_sum)
        return 

    for j in range(n):
        if visited[j]: continue
        visited[j] = True
        cur_sum += chessBoard[cur][j]
        findMax(cur+1)

        cur_sum -= chessBoard[cur][j]
        visited[j] = False


findMax(0)

print(max_sum)