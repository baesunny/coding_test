N = int(input())

def prime_sum(N):
    is_prime = [True] * (N + 1)
    is_prime[0] = is_prime[1] = False 
    for i in range(2, int(N**0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, N + 1, i):
                is_prime[j] = False
    
    primes = [x for x in range(2, N + 1) if is_prime[x]]
    
    count = 0
    start, end = 0, 0
    current_sum = 0

    while end <= len(primes):
        if current_sum == N:
            count += 1
            current_sum -= primes[start]
            start += 1
        elif current_sum < N:
            if end < len(primes):
                current_sum += primes[end]
            end += 1
        else:  # current_sum > N
            current_sum -= primes[start]
            start += 1

    return count

print(prime_sum(N))