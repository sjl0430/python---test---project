def solution(l, r):
    answer = []
    arr = ['0','5']
    for i in range(l, r+1):
        str1 = str(i)
        n = 0
        for s in str1:
            if s in arr:
                n += 1
            else:
                break
        if n == len(str1):
            answer.append(i)
    if answer == []:
        answer.append(-1)
    return answer