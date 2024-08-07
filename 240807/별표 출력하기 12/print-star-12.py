n = int(input())

st = ['*' for x in range(n)]
print(*st)

for x in range(0, n, 2):
    st[x] = ' '

for i in range(n-1):
    if st[i] == '*':
        st[i] = ' '
    print(*st)