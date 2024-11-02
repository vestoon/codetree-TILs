import sys
input = sys.stdin.readline

n = int(input())
grid = [list(map(int, input().split())) for x in range(n)]
visited = [[False for x in range(n)] for y in range(n)]

dx = (1, -1, 0, 0)
dy = (0, 0, 1, -1)
cnt_block = 0
M_size_block = 0

def dfs(i, j, cur):
    visited[i][j] = True
    cnt = 1

    for d in range(4):
        ni, nj = i+dx[d], j+dy[d]

        if 0<=ni<n and 0<=nj<n and not visited[ni][nj] and grid[ni][nj] == cur:
            cnt += dfs(ni, nj, cur)
    
    return cnt


for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            cur_size = dfs(i, j, grid[i][j])
            if cur_size >= 4:
                cnt_block += 1
            M_size_block = max(M_size_block, cur_size)
    
print(cnt_block, M_size_block)