def solution(record):
    answer = []
    user = {}
    for rec in record:
        check = rec.split()
        if rec.startswith("Leave") != True: # leave를 제외한 결과가 이름에 영향을 줌
            user[check[1]] = check[2] # 유저 정보 업데이트
    # check[1]: 입력 중 uid 부분
    # check[2]: 입력 중 닉네임 부분 
    for rec in record:
        check = rec.split()
        if rec.startswith("Enter"):
            answer.append(user[check[1]] +"님이 들어왔습니다.")
        elif rec.startswith("Leave"):
            answer.append(user[check[1]] +"님이 나갔습니다.")
    return answer


# uid의 value값으로 들낙 아웃풋을 변경
# uid : value 의 딕셔너리 구성
# Enter와 Change가 트리거 

print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))