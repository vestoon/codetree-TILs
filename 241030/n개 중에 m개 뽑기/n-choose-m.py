N, M = map(int, input().split())
"""
1~ N 중에 M개를 뽑을 수 있는 모든 경우의 수 구하기
중복 불가!

"""

def combination(acc):
    if len(acc) == M:
        print(*acc)
        return

    start = acc[-1] if acc else 0
    for nxt in range(start+1, N+1):
        combination(acc+[nxt])

combination([])