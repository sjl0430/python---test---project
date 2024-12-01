def solution(code):
    answer = ''
    mod = 0
    for i in range(0,len(code)):
        if(mod == 0):
            if(code[i] != '1' and i % 2 == 0):
                answer += code[i]
            elif(code[i] == '1'):
                mod = 1
        elif(mod == 1):
            if(code[i] != '1' and i % 2 == 1):
                answer += code[i]
            elif(code[i] == '1'):
                mod = 0
    if answer=='':
        answer = "EMPTY"
    return answer

print(solution("abc1abc1abc"))