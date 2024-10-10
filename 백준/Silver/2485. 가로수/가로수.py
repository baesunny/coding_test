import math

N = int(input())  # 이미 있는 나무 수
tree = [int(input()) for _ in range(N)]  # 이미 있는 나무 위치

distance = [] #간격
for i in range(N - 1):
    distance.append(tree[i + 1] - tree[i])

gcd = distance[0]
for i in range(1, len(distance)):
    gcd = math.gcd(gcd, distance[i]) #간격들간의 최대공약수

result = 0
for d in distance:
    result += (d // gcd) - 1

print(result)