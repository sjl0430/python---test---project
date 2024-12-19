def solution(s):
    answer = [] # 빈 리스트 생성
    count = 0 # 변환 횟수
    zero_count = 0 # 발견한 0의 개수

    while True: # 반복한다
        if s == "1": # s가 1일 때
            break #까지
        zero_count += s.count("0") # 현재 문자열 s에 있는 '0'의 수 카운트
        s = s.replace("0", "") # 문자열 s에 있는 '0' 제거
        # replace("a","b")는 문자열 내의 'a'를 'b'로 바꾸어주는데 'b' 자리의 값을 비워 ""을 두면
        # 문자열에 있는 'a'가 사라진다.
        s = bin(len(s))[2:]# bin()으로 직전 s(문자열 -> 십진수)의 값을 다시 2진수로 변경 
        # bin()을 사용한 결과값은 0b이진수(데이터 타입은 문자열)로 출력되기 때문에 '0b'도 제거
        count += 1 # 시행 횟수 카운트
    answer = [count, zero_count] # 정답 장전
    return answer # 발사

print(solution(input()))