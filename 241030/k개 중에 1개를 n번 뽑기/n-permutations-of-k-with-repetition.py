N, K = map(int, input().split())

def recur(acc:list, cnt:int):
    if cnt == N:
        print(*acc)
        return 
    
    for nxt in range(1, K+1):
        recur(acc+[nxt], cnt+1)

recur([], 0)