n = int(input())


# 길이가 n일 때 체킹 먼저
def sol(cur):
    if len(cur) == n:
        for l in range(1, n//2 + 1):

            for i in range(n - 2*l+1):

                for j in range(i, i+l):
                    if cur[j] != cur[j+l]:
                        break
                else: # 부분수열이 일치하는 경우
                    return False
    
        print(cur)
        return True
    
    for nxt in ['4', '5', '6']:
        if nxt == cur[-1]:
            continue
        if sol(cur+nxt):
            return True

sol('4')