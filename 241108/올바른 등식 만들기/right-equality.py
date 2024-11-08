import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(map(int ,input().split()))

dp = [0 for x in range(41)] # -20 ~ 20 까지 인덱싱 가능
dp[0] = 1

for a in arr:
    tmp = [0 for x in range(41)]

    for i in range(-20, 21):
        if dp[i] <= 0: continue

        if i+a <= 20:
            tmp[i+a] += dp[i]
        if -20 <= i-a:
            tmp[i-a] += dp[i]

    dp = tmp

print(dp[M])