import sys
sys.setrecursionlimit(10**7)

def solution(k, room_number):
    answer = []
    stay = []
    remain = {}
    
    for i in room_number:
        room = i
        stay = [room]
        
        while room in remain:
            room = remain[room]
            stay.append(room)
        
        answer.append(room)
        
        for j in stay:
            remain[j] = room+1    
            
    return answer


# print(solution(10, [1,3,4,1,3,1]))

#딕셔너리