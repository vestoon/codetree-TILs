n = int(input())

st = ['*' for x in range(n)]
print(*st)
for i in range(1,n-1):
    st[i] = ' '

for i in range(n-1):
    st[i] = '*'
    print(*st)