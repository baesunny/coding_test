import sys
input = sys.stdin.read
data = input().splitlines()

T = int(data[0])  # 테스트 케이스 수
results = []

index = 1
for _ in range(T):
    N, M = map(int, data[index].split())  # 국가 수 N, 비행기 종류 M
    index += 1 + M  # 현재 테스트 케이스의 모든 입력 건너뛰기
    results.append(N - 1)  # MST의 간선 수는 항상 N-1

# 결과 출력
print("\n".join(map(str, results)))
