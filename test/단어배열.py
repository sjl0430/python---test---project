def count_letters(s):
    # 모음과 자음 집합 정의
    vowels = set('AEIOU')
    consonants = set('BCDFGHJKLMNPQRSTVWXZ')
    
    # 각 문자 유형별 카운터 초기화
    count_v = 0  # 모음 카운터
    count_c = 0  # 자음 카운터
    count_y = 0  # Y 카운터
    ng_count = 0  # NG 카운터

    i = 0

    while i < len(s):
        char = s[i]
        if char == 'N' and i + 1 < len(s) and s[i + 1] == 'G':
            if i > 0 and i + 2 < len(s) and s[i-1] in vowels and s[i+2] in vowels: 
                count_c += 1 # NG가 모음 사이에 있으면 각자도생
            else:
                ng_count += 1
                i += 1  # NG를 하나의 자음으로 처리하므로 다음 문자 건너뛰기
        elif char in vowels:
            count_v += 1
        elif char in consonants:
            count_c += 1
        elif char == 'Y':
            count_y += 1
        i += 1

    return count_v, count_c, count_y, ng_count

def calculate_max_word_length(vowel_count, consonant_count, y_count, ng_count):
    # Y를 모음과 자음 모두로 사용 가능하므로 각각에 더해줌
    max_vowels = vowel_count + y_count
    max_consonants = consonant_count + ng_count + y_count
    
    # 최대 음절 수 계산: 모음 수와 자음 수의 절반 중 작은 값
    max_syllables = min(max_vowels, max_consonants // 2)
    
    # 각 음절은 3글자(CVC)로 구성되므로 3을 곱함
    if ng_count == 0:
        return max_syllables * 3
    else:
        return max_syllables * 3 + ng_count

def find_longest_word(s):
    # 문자열에서 각 문자 유형별 개수 세기
    vowels, consonants, ys, ngs = count_letters(s)
    # 최대 단어 길이 계산
    return calculate_max_word_length(vowels, consonants, ys, ngs)

# 사용 예시
print(find_longest_word("ICPCJAKARTA"))  # 예상 출력: 9
print(find_longest_word("NGENG"))        # 예상 출력: 5
print(find_longest_word("YYY"))          # 예상 출력: 3
print(find_longest_word("DANGAN"))       # 예상 출력: 6
print(find_longest_word("AEIOUY"))       # 예상 출력: 0