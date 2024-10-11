from math import gcd

a, b = map(int, input().split())
A, B = map(int, input().split())

son = a * B + A * b  # 분자
mom = b * B           # 분모

gcd = gcd(son, mom)

final_son = son // gcd
final_mom = mom // gcd

print(final_son, final_mom)