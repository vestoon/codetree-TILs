n = int(input())
score = ['F' for x in range(60)]
for _ in range(10):
    score.append('D')
for _ in range(10):
    score.append('C')
for _ in range(10):
    score.append('B')
for _ in range(11):
    score.append('A')

for x in range(n, 101):
    print(score[x], end=' ' )