N, M = map(int, input().split())

def sequence(N, M, lst=[]):
    if len(lst) == M:
        print(' '.join(map(str, lst)))
        return
    
    start = lst[-1] if lst else 1
    
    for i in range(start, N + 1):
        sequence(N, M, lst + [i])

sequence(N, M)