def solution(citations):
    answer = 0
    index = sorted(citations,reverse=True)
    for i in range(len(index)):
        if index[i] < i + 1:
            answer = i
            break
        else:
            answer = len(index)
    
    return answer