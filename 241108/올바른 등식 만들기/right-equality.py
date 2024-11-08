import sys
input = sys.stdin.readline

"""
숫자 N개 
처음부터 N까지 순서대로 더하거니 빼서 그 합이 M이 되는 가짓수
+-20을 넘으면 안된다 

더할 건지 뺄 건지는 자유롭게 선택 가능


-20 ~ 20 까지 dp 사용
들어가는 값은 경우의 수
초기화 0
"""

N, M = map(int, input().split())
arr = list(map(int ,input().split()))

dp = [0 for x in range(41)] # -20 ~ 20 까지 인덱싱 가능
dp[arr[0]] = 1
dp[-arr[0]] = 1

for a in arr[1:]:
    tmp = [0 for x in range(41)]

    for i in range(-20, 21):
        if not dp[i]: continue

        if i+a < 20:
            tmp[i+a] += dp[i]
        if -20 < i-a:
            tmp[i-a] += dp[i]

    dp = tmp
# print(dp)
print(dp[M])