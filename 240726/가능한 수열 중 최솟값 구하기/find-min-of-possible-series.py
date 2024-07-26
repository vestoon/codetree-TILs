n = int(input())

ans = []
avoid = [False for x in range(7)]


while len(ans) != n:
    for nxt in range(4, 7):
        if avoid[nxt]:
            continue
        ans.append(nxt)

        for l in range(1, len(ans)//2 + 1):
            for i in range(len(ans)-2*l, len(ans)-l):
                if ans[i] != ans[i+l]:
                    break
            else: # 일치하는 부분수열 발생
                break
        else: # 일치하는 부분수열이 하나도 없음
            avoid = [False for x in range(7)]
            break # 종료하고 다음 while문으로
        #일치하는 부분수열이 있기 때문에
        # 넣은거 취소하고  다시 반복
        ans.pop()
    else: # 아무 것도 넣지 못함
        avoid[ans[-1]] = True
        ans.pop() # 하나 더 빼야 함
        
for x in ans:
    print(x, end='')