from itertools import permutations

def prime_number(n):
    if n < 2:
        return False # 소수는 2 이상이어야 하니까!
    
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False  # 나누어 떨어지는 값이 없어야 함.
    return True

def solution(number):
    numbers = set()  #처음에 빈리스트로 했다가 중복 안되는 걸 고려해서 set으로 변경
    for i in range(1, len(number) + 1):
        for p in permutations(number, i):
            num = int(''.join(p))
            numbers.add(num)
    
    count = 0
    for num in numbers:
        if prime_number(num):
            count += 1
    
    return count
