import sys
import collections
input = sys.stdin.readline

dx = (1, -1, 0, 0)
dy = (0, 0, 1, -1)
n, k, m = map(int, input().split())

grid = [list(map(int, input().split())) for x in range(n)]
stones = []
sources = []
ans = 0 # 방문 가능한 서로 다른 칸의 최대값

for i in range(n):
    for j in range(n):
        if grid[i][j]:
            stones.append((i, j))

for _ in range(k):
    r, c = map(int, input().split())
    sources.append((r-1, c-1))

def bfs()-> int:
    # for z in grid:
    #     print(*z)
    visited = [[False for x in range(n)] for y in range(n)]
    for i, j in sources:
        visited[i][j] = True
    que = collections.deque(sources)
    ret = k

    while que:
        cur_i, cur_j = que.popleft()

        for d in range(4):
            nxt_i, nxt_j = cur_i+dx[d], cur_j+dy[d]

            if 0<=nxt_i<n and 0<=nxt_j<n and not visited[nxt_i][nxt_j] and not grid[nxt_i][nxt_j]:
                visited[nxt_i][nxt_j] = True
                que.append((nxt_i, nxt_j))
                ret += 1
    # print(ret)
    return ret

def comb(i, cnt_stone): # comb(0, 0)
    global ans
    if cnt_stone == m:
        ans = max(ans, bfs())
        return
    if i == len(stones):
        return

    cur_i, cur_j = stones[i]
    grid[cur_i][cur_j] = 0

    comb(i+1, cnt_stone+1)

    grid[cur_i][cur_j] = 1
    comb(i+1, cnt_stone)

comb(0, 0)
print(ans)