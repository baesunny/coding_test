n, m = map(int, input().split())

dms = set(input() for i in range(n))
bms = set(input() for i in range(m))

common = sorted(dms & bms)

# 결과 출력
print(len(common))
for i in common:
    print(i)