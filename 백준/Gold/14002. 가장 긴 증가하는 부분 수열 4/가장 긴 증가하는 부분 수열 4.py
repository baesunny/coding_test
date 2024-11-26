N = int(input())
A = list(map(int, input().split()))

def longest_one(N, A):
    dp = [1] * N
    parent = [-1] * N
    
    for i in range(1, N):
        for j in range(i):
            if A[j] < A[i]:
                if dp[j] + 1 > dp[i]:
                    dp[i] = dp[j] + 1
                    parent[i] = j
    
    max_len = max(dp)
    max_index = dp.index(max_len)
    
    subsequence = []
    while max_index != -1:
        subsequence.append(A[max_index])
        max_index = parent[max_index]
    subsequence.reverse()
    return max_len, subsequence

length, subsequence = longest_one(N, A)

print(length)
print(" ".join(map(str, subsequence)))