N, M = map(int,input().split())

from itertools import combinations
choice = combinations(range(1, N + 1), M)

for i in choice:
    print(" ".join(map(str, i)))