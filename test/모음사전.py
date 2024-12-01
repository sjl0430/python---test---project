def solution(word):
    w = word
    answer = 0
    
    for i in range(len(w)):
        if w[i] == 'A':
            answer += 1
        elif w[i] == 'E':
            answer += count(2, 3, i)
        elif w[i] == 'I':
            answer += count(3, 2, i)
        elif w[i] == 'O':
            answer += count(4, 1, i)
        elif w[i] == 'U':
            answer += count(5, 0, i)
        
    return answer
    
def count(num, dec, n):
    while(n != 4):
        num = num * 5 - dec
        n += 1
    return num

# print(solution("E"))