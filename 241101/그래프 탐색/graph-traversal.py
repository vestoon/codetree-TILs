import sys
input = sys.stdin.readline

N, M = map(int, input().split())
adj_list = [[] for x in range(N+1)]
visited = [False for x in range(N+1)]

for _ in range(M):
    x, y = map(int, input().split())
    adj_list[x].append(y)
    adj_list[y].append(x)
cnt = 0

def dfs(cur):
    # print(cur)
    global cnt
    cnt += 1

    for nxt in adj_list[cur]:
        if not visited[nxt]:
            visited[nxt] = True
            dfs(nxt)

visited[1] = True
dfs(1)
print(cnt -1)