from collections import Counter

N = int(input())
number = list(map(int, input().split()))
M = int(input())
count = list(map(int, input().split()))

sang_card = Counter(number)
result = [sang_card[query] for query in count]
print(*result)