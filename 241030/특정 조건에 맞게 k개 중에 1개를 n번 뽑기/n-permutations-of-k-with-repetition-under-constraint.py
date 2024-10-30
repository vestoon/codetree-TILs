K, N = map(int, input().split())


def recur(acc, comb):
    if len(acc) == N:
        print(*acc)
        return

    
    for nxt in range(1, K+1):
        if nxt != acc[-1]:
            recur(acc+[nxt], 1)
            continue

        if comb == 2: continue
        recur(acc+[nxt], comb+1)

for i in range(1, K+1):
    recur([i], 1)