m = [30 for x in range(13)]
m[2] = 28
for i in range(1,13,2):
    m[i] = 31

n = int(input())
print(m[n])