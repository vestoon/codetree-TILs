import sys
input = sys.stdin.readline


"""
무게 M을 넘지 않으면서 보석의 가치합을 최대가 되도록 하기

무게 기준으로 dp 를 구현,

완탐 돌리면 복잡도는 이번에도 nm ? 
"""

N, M = map(int, input().split()) # N: 보석 개수, M: 최대 무게
dp = [0 for x in range(M+1)] # 무게 i로 조합할 수 있는 최대 가치
jewels = []

for _ in range(N):
    w, v = map(int, input().split())
    jewels.append((w, v))

for i in range(M+1):

    for w, v in jewels:
        if i+w > M: continue

        dp[i+w] = max(dp[i+w], dp[i]+v)

print(max(dp))