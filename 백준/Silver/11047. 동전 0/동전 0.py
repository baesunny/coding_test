N, K = map(int, input().split())

def coin(N, K, coins):
    count = 0   
    for i in range(N-1, -1, -1):
        if K == 0:
            break
        count += K // coins[i]
        K %= coins[i]
    return count

coins = [int(input().strip()) for _ in range(N)]
print(coin(N, K, coins))