def solution(arr, queries):
    answer = []
    for s,e,k in queries:
        temp = []
        p = 1000000
        for i in range(s,e+1):
            temp.append(arr[i])
        for i in temp:
            if k < i:
                p = i if i < p else p
        if p != 1000000:
            answer.append(p)
        else:
            answer.append(-1)
    return answer

solution([0, 1, 2, 4, 3],[[0, 4, 2],[0, 3, 2],[0, 2, 2]])