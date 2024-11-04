import sys
from collections import deque
input = sys.stdin.readline

dy = (1, -1, 0, 0)
dx = (0, 0, 1, -1)

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for x in range(n)]

def bfs(i, j):
    que = deque()
    que.append((i, j))
    visited = [[False for x in range(m)] for y in range(n)]
    visited[i][j] = True
    ret = 0

    while que:
        l = len(que)
        for _ in range(l):
            cur_i, cur_j = que.popleft()
            if cur_i == n-1 and cur_j == m-1:
                return ret

            for d in range(4):
                nxt_i, nxt_j = cur_i+dx[d], cur_j+dy[d]

                if 0<=nxt_i<n and 0<=nxt_j<m and not visited[nxt_i][nxt_j] and grid[nxt_i][nxt_j]:
                    que.append((nxt_i, nxt_j))
                    visited[nxt_i][nxt_j] = True
        ret += 1

print(bfs(0, 0))