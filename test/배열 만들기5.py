def solution(intStrs, k, s, l):
    answer = []
    for i in intStrs:
        if(int(i[s:s+l]) > k):
            answer.append(i[s:s+l])
    return answer

solution(["0123456789","9876543210","9999999999999"],50000,5,5)