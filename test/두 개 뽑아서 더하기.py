from itertools import permutations

def solution(numbers):
    answer = []
    num = list(permutations(numbers, 2))
    for i in range(len(num)):
           answer += [num[i][0] + num[i][1]]
    answer = sorted(list(set(answer)))
    
    return answer