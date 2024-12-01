from itertools import permutations

def solution(numbers):
    answer = []
    arr = []
    num = []
    for i in range(len(numbers)):
        arr += list(permutations(numbers, i+1)) 
            
    for i in arr:
        num += [int(''.join(i))]
        
    for i in num:
        if prime(i):
            answer += [i]
    
    answer = len(set(answer))
    return answer


def prime(num):
    if num < 2:
        return False
    i = 2
    while i * i <= num:
        if num % i == 0:
            return False 
        i += 1
    return True