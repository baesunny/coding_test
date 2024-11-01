# 내가 제일 자신있게 적은 유일한 코드
s = input().strip()

def reverse_words_in_string(s: str) -> str:
    result = []
    i = 0
    n = len(s)

    while i < n:
        if s[i] == '<':
            # 태그 발견 >> 태그 전체를 result에 반환
            tag_end = s.find('>', i) + 1
            result.append(s[i:tag_end])
            i = tag_end
        else:
            # 단어 발견 >> 뒤집어서 result에 반환
            word_start = i
            while i < n and s[i] not in ['<', ' ']:
                i += 1
            result.append(s[word_start:i][::-1])  # [::-1]를 쓰면 단어 뒤집기
            
            # 공백이 있으면 결과에 추가
            if i < n and s[i] == ' ':
                result.append(' ')
                i += 1  # 공백 건너뛰기

    return ''.join(result)

print(reverse_words_in_string(s))