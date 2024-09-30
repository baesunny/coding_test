T = int(input())

import math
for i in range(T):
    N, M = map(int, input().split())
    result = math.comb(M, N)
    print(result)