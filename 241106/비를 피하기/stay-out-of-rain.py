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
    visited = [[False for x in range(n)] for y in range(n)]
    visited[i][j] = True
    distance = 0

    while que:
        l = len(que)
        # print(que)
        for _ in range(l):
            cur_i, cur_j = que.popleft()

            if grid[cur_i][cur_j] == 3:
                answer[i][j] = distance
                return

            for d in range(4):
                nxt_i, nxt_j = cur_i+dx[d], cur_j+dy[d]

                if 0<=nxt_i<n and 0<=nxt_j<n and not visited[nxt_i][nxt_j] and grid[nxt_i][nxt_j] != 1:
                    visited[nxt_i][nxt_j] = True
                    que.append((nxt_i, nxt_j))

        # print(d)      
        distance += 1
    
    answer[i][j] = -1
    return

for i in range(n):
    for j in range(n):
        if grid[i][j] == 2:
            bfs(i, j)


for line in answer:
    print(*line)