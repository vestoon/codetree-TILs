import sys
"""
n: 턴의 수
m: 윷놀이 판의 길이
k: 말의 수
"""
n, m, k = map(int, input().split())
distances = list(map(int, input().split())) # 움직일 수 있는 최대 거리 
max_score = 0 # 최대 점수
cur_score = 0 # 재귀가 진행되는 동안 현제 점수
cur_state = [1 for x in range(k)] # 각 말의 현재 위치


def recur(i):
    global cur_score, max_score
    if i == n:
        max_score = max(max_score, cur_score)
        return 
    
    for j in range(k):
        if cur_state[j] >= m:
            max_score = max(max_score, cur_score)
            continue # 백트레킹

        cur_state[j] += distances[i]
        if cur_state[j] >= m:
            cur_score += 1

        recur(i+1)

        if cur_state[j] >= m:
            cur_score -= 1
        cur_state[j] -= distances[i]

recur(0)
print(max_score)