n = int(input())

ans = []
avoid = 0

while len(ans) != n:
    # print(len(ans), end=' ')
    # for _ in range(4, 7):
    #     print(1 if avoid[_] else -1, end=' ')
    # print()

    for nxt in range(4, 7):
        if nxt == avoid:
            continue
        ans.append(nxt) # 일단 넣어봄
        flag = False

        for l in range(1, len(ans)//2 + 1): # 모든 길이에 대해서 일치하는 수열이 있는지 검사
            for i in range(len(ans)-2*l, len(ans)-l): # 탐색 시작 지점
                if ans[i] != ans[i+l]:
                    break
            else: # 일치하는 부분수열 발생
                flag = True
            
            if flag: break
        
        if flag: # nxt 빼기
            ans.pop()
        else:
            break
    else: # break가 안걸렸으므로 조건에 맞는 nxt 를 찾지 못했을 때
        avoid = ans[-1]
        # print('p', ans[-1])
        ans.pop()
        continue

    avoid = 0
    # print()

for x in ans:
    print(x, end='')