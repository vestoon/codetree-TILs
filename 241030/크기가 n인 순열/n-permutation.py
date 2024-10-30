n = int(input())
arr = [x for x in range(1, n+1)]

def permutation(acc, rest):
    if len(rest) == 1:
        print(*(acc+rest))
        return 

    for i in range(len(rest)):
        permutation(acc+[rest[i]], rest[:i]+rest[i+1:])
    

permutation([], arr)