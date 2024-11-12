import sys
input = sys.stdin.readline

"""
비슷한 수열 : 인접한 두 숫자가 다른 횟수가 M번 이하
유사도: 두 수열 간에 같은 위치에 같은 원소가 나온 횟수

수열이 주어질 때 비슷한 수열이면서 유사도가 가장 높은 수열을 구해보자

수열이 계속 같은 수가 나와야 하는데 숫자가 바뀔수 있는게 M번이라는 것
총 최대 M+1개의 구간이 생길 수 있다.  

i번째에서 숫자가 x 로 바뀐다면 arr[i]랑 일치하는 숫자로 바꾸는 것이 무조건 유리

어떤 값을 선택해서 최선인지 알아야 한다? 그래야 한칸 건너서 같은 값이 나와도 감지할  수 있음
숫자의 종류가 1~4밖에 안되는것도 이 때문인듯?

무조건 숫자를 바꾸는 것이 정답이 아닐 수도 있다. 
마지막 숫자를 저장하는 세 번재 인덱스가 존재해야 최선의 선택인지 아닌지 알 수 있다. 
i 번째 위치까지 숫자를 j번 변경하면서 왔고, 현재 마지막 숫자는 k 이다. 

dp[i-1][j][k] 에서 그대로 넘어온 경우의 수
dp[i-1][j-1][not k] 에서 한 번 변경한 경우의 수

dp[i][j][k] : max(dp[i-1][j][k], 

"""

N, M = map(int, input().split())
arr = list(map(int, input().split()))
# dp[i][j] i번재까지 숫자를 j번 바꾸고 마지막 숫자가 k일 때 최대 유사도 
dp = [[[0 for k in range(5)] for j in range(M+1)] for i in range(N)]

# dp[0][0][1] ~ dp[0][0][4] 초기 조건 설정
for k in range(1, 5):
    dp[0][0][k] = 1 if arr[0] == k else 0

for i in range(1, N):
    for j in range(M+1):
        for k in range(1, 5):
            # dp[i][j][k]

            for pk in range(1, 5):
                if k == pk: # 이전 값에서 변경하지 않는 경우
                    if arr[i] == pk: # 변경하지 않았는데 이전 값과 i번째 수열의 값이 일치하는 경우
                        dp[i][j][k] = max(dp[i][j][k], dp[i-1][j][pk] + 1)
                    else: # 값을 변경하지도 않았고 현재 수열의 값과 일치하지도 않는 경우
                        dp[i][j][k] = max(dp[i][j][k], dp[i-1][j][pk])
                else: # 마지막 값이 pk에서 k로 바꾸는 경우
                    if arr[i] == k: # 바꾼 k가 수열의 현재 값과 일치하는 경우
                        dp[i][j][k] = max(dp[i][j][k], dp[i][j-1][pk] + 1)
                    else: # 마지막 값을 pk에서 k로 바뀠지만 수열의 현재 값과 일치하지는 않는 경우
                        dp[i][j][k] = max(dp[i][j][k], dp[i][j-1][pk])

ans = 0 
for j in range(M+1):
    for k in range(1, 5):
        ans = max(ans, dp[N-1][j][k])

print(ans)
