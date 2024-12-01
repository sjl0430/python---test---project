def solution(phone_book):
    answer = True
    num = sorted(phone_book) # 사전식 순서 정렬
    hashMap = dict(zip(num, num[1:])) # key: 0번부터 n-1번, value: 1번부터 n번

    for n1, n2 in hashMap.items():
        if n2.startswith(n1): # 문자열 n2가 n1의 내용으로 시작하면 True
            answer = False
            break # 검거 완료시 종료
    return answer

solution(["123","456","789"])
