import sys
import collections
input = sys.stdin.readline

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for y in range(n)]

dy = (1, -1, 0, 0)
dx = (0, 0, 1, -1)

que = collections.deque()
que.append((0, 0))
grid[0][0] = 0

if not grid[n-1][m-1]:
    print(0)
    exit()

while que:
    i ,j = que.popleft()

    for d in range(4):
        ni, nj = i+dx[d], j+dy[d]
        if 0<=ni<n and 0<=nj<m and grid[ni][nj]:
            grid[ni][nj] = 0
            que.append((ni, nj))

print(0 if grid[m-1][n-1] else 1)