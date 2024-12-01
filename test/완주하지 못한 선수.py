from collections import Counter

def solution(participant, completion):
    answer = ''
    hash1 = Counter(participant) - Counter(completion)
    # 완주 실패한 사람은 참가자 중 한 명, 동명이인 가능
    # => 이름별 참가자 수 - 이름별 완주자 수
    # 그 중 유일하게 value가 1인 딕셔너리의 key 값
    # (또는 2차원 리스트의 [x][0]값)
    
    hash1 = Counter(hash1).most_common(1)
    # 가장 value가 큰 것 순으로 리스트 생성
    
    answer = hash1[0][0]
    # 가장 value가 컸던 key의 값의 리스트 위치
    return answer