from collections import Counter
# 이후에 사용할 Counter 클래스를 위한 모듈  

def solution(clothes):
    answer = 0
    mix = 1
    wear = dict(clothes)
    counts = Counter(wear.values()).values()
    # 딕셔너리 wear의 각 value의 빈도를 정리한 딕셔너리의 각 value로 만든 리스트
    # wear.values() ==> dict_values(['headgear','eyewear','headgear'])
    # Counter(wear.values()) ==> Counter({'headgear': 2, 'eyewear': 1})
    # Counter(wear.values()).values() ==> dict_values([2, 1])
    # 즉, 각 의상의 종류별 이름 개수
   
    for i in counts: # 의상의 종류별 이름 개수
            mix *= i+1 # 각 옷을 안 입는 경우 생각
    answer = mix -1 # 뭐라도 걸쳐야 함
    return answer

    # 딕셔너리의 value에는 리스트를 넣을 수 있음

