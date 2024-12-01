from itertools import permutations

def solution(expression):
    answer = 0
    operators = ['+', '-', '*'] # 사용하는 연산자 삼형제
    operator_permutation = list(permutations(operators, 3)) # 연산자의 6가지 리스트
    expression = expression.replace('+', ' + ')
    expression = expression.replace('-', ' - ')
    expression = expression.replace('*', ' * ')
    # 거리두기 삼형제
    expression = expression.split() #손절시킴
    for operator in operator_permutation: # 연산자 컴 온
        temp_expression = expression.copy() # 내용을 바꿀 예정이라 본체를 계속 카피함 
        # 깊은 복사하는 이유는 expression을 수정하면 안되기 때문 왜냐하면 다음 연산자 순열을 위해 원본이 필요하기 때문
        for op in operator: # 연산자 우선순위 순서
            while op in temp_expression: # 우선 순위 먼저 계산
                idx = temp_expression.index(op) # 연산자의 인덱스 번호 찾기
                temp_expression[idx-1] = str(eval(temp_expression[idx-1] + op + temp_expression[idx+1]))
                # eval은 문자로 이루어진 연산자들의 연산을 진행시킴
                # 연산자 앞의 숫자와 뒤의 숫자를 연산자로 계산한 결과를 
                # 연산자 앞의 숫자에 저장 예를 들어 1+2 * 3이면 1+6 이렇게 저장
                temp_expression.pop(idx+1) # 연산자 뒤의 숫자 삭제
                temp_expression.pop(idx) # 연산자 삭제 
                # 삭제한 연산자와 연산자 뒤의 숫자를 삭제했기 때문에 연산자 앞의 숫자만 남음
                # 삭제한 이유는 연산자를 계산했기 때문에 필요가 없어졌기 때문
        answer = max(answer, abs(int(temp_expression[0])))
        # 0번째 인덱스에는 연산자가 없는 숫자만 남아있기 때문에 절대값을 취한후 최대값을 찾음
    return answer # 답 리턴


    