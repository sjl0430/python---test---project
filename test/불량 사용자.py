from itertools import permutations

def solution(user_id, banned_id):
    answer = 0
    p_id = list(permutations(user_id, len(banned_id)))
    arr = []
    for i in p_id:
        if check(i, banned_id):
            i = set(i)
            if i not in arr:
                arr += [i]
                
    answer = len(arr)
    return answer


def check(user, banned):
    for i in range(len(banned)):
        if len(user[i]) != len(banned[i]):
            return False
        
        for j in range(len(user[i])):
            if banned[i][j] != "*" and banned[i][j] != user[i][j]:
                return False
    return True
        