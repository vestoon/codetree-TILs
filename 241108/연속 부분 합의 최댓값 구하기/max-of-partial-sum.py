import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

"""
dp[i] : i로 끝나는 연속된 부분수열 중 가장 합이 큰 값

dp[i] = dp[i] or dp[i]+dp[i+1] ? 
"""

dp = arr[:]

for i in range(1, n):
    if dp[i-1] > 0:
        dp[i] += dp[i-1]

print(max(dp))