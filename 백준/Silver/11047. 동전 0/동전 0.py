N, K = map(int, input().split())
coins = [int(input().strip()) for i in range(N)]

def coin(N, K, coins):
    cnt = 0   
    for i in range(N-1, -1, -1):
        if K == 0:
            break
        cnt += K // coins[i]
        K %= coins[i]
    return cnt

print(coin(N, K, coins))