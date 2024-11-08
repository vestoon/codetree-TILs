import sys
input = sys.stdin.readline

"""
합이 m이 되는 최소 길이의 부분수열, 연속하지 않아도 된다?
수열의 원소는 전부 양수

완탐 2^n

1~ x 까지 
dp[x] = x 를 만드는데 필요한 최소 부분 수열의 길이? 
m 값이 10,000 이하라는 점을 생각하면  m 사이즈의 dp 배열 생성 후 
모든 원소에 대해 반복하면 mn 정도? 정렬하면 줄일 수 있나?

각 원소는 한 번씩만 쓸 수 있다!
"""

n, m = map(int, input().split()) # n: 수열의 길이, m: 만들고자 하는 값
A = list(map(int, input().split())) # 

dp = [n+1 for x in range(m+1)]
dp[0] = 0

for a in A:

    for i in range(m, -1, -1):
        if i-a < 0: continue

        dp[i] = min(dp[i], dp[i-a]+1)

# print(dp)
print(dp[m] if dp[m] <= n else -1)