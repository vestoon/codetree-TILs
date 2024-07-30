acc= 0
cnt = 0
while True:
    n = int(input())
    if not (20 <= n <30):
        break
    
    acc += n
    cnt += 1

print(f"{acc/cnt:.2f}")