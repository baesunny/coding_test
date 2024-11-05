import sys
import heapq

# 입력을 한 번에 읽어와 줄 단위로 나누어 리스트로 저장
input = sys.stdin.read
operations = input().splitlines()

# 절댓값 힙을 저장할 리스트
abs_heap = []

# 첫 번째 줄: 연산의 개수
num_operations = int(operations[0])

# 결과를 저장할 리스트
results = []

for i in range(1, num_operations + 1):
    value = int(operations[i])
    if value != 0:
        # 절댓값 힙에 (절댓값, 실제 값) 형태로 저장
        heapq.heappush(abs_heap, (abs(value), value))
    else:
        # value가 0이면 절댓값이 가장 작은 값을 출력
        if abs_heap:
            results.append(heapq.heappop(abs_heap)[1])
        else:
            results.append(0)

# 결과 출력
print("\n".join(map(str, results)))
