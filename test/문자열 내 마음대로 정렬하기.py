def solution(strings, n):
    answer = []
    arr = []
    
    for i in strings:
        arr += [i[n]]
    
    arr = sorted(arr)
    strings = sorted(strings)
    
    for i in range(len(arr)):
        for j in strings:
            if arr[i] == j[n]:
                if j not in answer: 
                    answer += [j]
    return answer