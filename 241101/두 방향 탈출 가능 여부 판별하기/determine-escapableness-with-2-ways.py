import sys
input = sys.stdin.readline

n , m = map(int, input().split())
grid = [list(map(int, input().split())) for x in range(n)]
visited = [[False for x in range(m)] for y in range(n)]


def dfs(i, j):
    visited[i][j] = True
    if i == n-1 and j == m-1:
        return True

    if j<m-1 and grid[i][j+1]:
        if not visited[i][j+1] and dfs(i, j+1):
            return True
    if i<n-1 and grid[i+1][j]:
        if not visited[i+1][j] and dfs(i+1, j):
            return True
    
    return False

if dfs(0, 0):
    print(1)
else:
    print(0)