A, B, C = map(int, input().split())

# A를 B번 곱한 결과를 C로 나눈 나머지를 저장할 변수
result = 1
current_product = A % C  # A를 C로 나눈 나머지로 초기화

# B가 0이 될 때까지 반복
while B > 0:
    if B % 2 == 1:  # B가 홀수일 경우
        result = (result * current_product) % C  # 결과에 현재 곱셈을 추가
    current_product = (current_product * current_product) % C  # 현재 곱셈 제곱
    B //= 2  # B를 반으로 나누기

print(result)