import sys
input = sys.stdin.readline

def sol():
    N, M = map(int, input().split())
    coins = list(map(int, input().split()))
    # print(coins)
    dp = [0 for x in range(M+1)]
    for coin in coins:
        if coin > M: continue
        dp[coin] = 1


    for i in range(M+1):
        if not dp[i]: continue

        for coin in coins:
            if i+coin > M: continue
            # print(i, coin)
            dp[i+coin] = min(dp[i+coin], dp[i]+1) if dp[i+coin] else dp[i]+1
        
        # print(i, dp)
    
    print(dp[M] if dp[M] else -1)

sol()