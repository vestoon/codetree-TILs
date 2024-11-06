import sys
from collections import deque

dx = (0, 0, 1, -1)
dy = (1, -1, 0, 0)

n, h, m = map(int, input().split())
grid = [list(map(int, input().split())) for y in range(n)]
answer = [[0 for x in range(n)] for y in range(n)]

def bfs(i, j):
    que = deque()
    que.append((i, j))
    distance = [[sys.maxsize for x in range(n)] for y in range(n)]
    distance[i][j] = 0

    while que:
        cur_i, cur_j = que.popleft()
        # print(cur_i, cur_j)

        if grid[cur_i][cur_j] == 3:
            answer[i][j] = distance[cur_i][cur_j]
            return

        for d in range(4):
            nxt_i, nxt_j = cur_i+dx[d], cur_j+dy[d]

            if 0<=nxt_i<n and 0<=nxt_j<n and distance[nxt_i][nxt_j] > distance[cur_i][cur_j]+1 and grid[nxt_i][nxt_j] != 1:
                distance[nxt_i][nxt_j] = distance[cur_i][cur_j] + 1
                que.append((nxt_i, nxt_j))

    answer[i][j] = -1
    return

for i in range(n):
    for j in range(n):
        if grid[i][j] == 2:
            bfs(i, j)


for line in answer:
    print(*line)