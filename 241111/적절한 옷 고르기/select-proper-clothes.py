import sys
input = sys.stdin.readline

N, M = map(int, input().split())
# dp[i][j] # i일 기준으로 지금 입은 옷이 j일 때의 최대값
dp = [[-1 for x in range(N)] for y in range(M+1)] # 날짜는 1부터 센다 불가능한 경우는 -1 처리해야 함

clothes = []
for _ in range(N): 
    # 날짜 1~M
    s, e, v = map(int, input().split()) # s~e 까지 입을 있고 화려함이 v 
    clothes.append((s, e, v))

for n in range(N): # 첫 번째 날에 대한 처리
    s, e, v = clothes[n]
    if s<=1<=e:
        dp[1][n] = 0

# 이후 두 번째 날부터 처리
for i in range(2, M+1):
    # print('i', i)
    for j in range(N):
        # print('j', j)
        s, e, v = clothes[j]
        if not (s<=i<=e): continue

        for pj in range(N):
            if dp[i-1][pj] == -1: continue #  i-1 번째 날에 pj의 옷을 입는 경우의 수가 없다면 continue
            ps, pe, pv = clothes[pj]
            # print(ps, pe, pv, dp[i-1][pj], abs(v-pv))
            dp[i][j] = max(dp[i][j], dp[i-1][pj] + abs(v-pv))
    
# print(clothes)
# for x in dp:
#     print(*x)
print(max(dp[M]))