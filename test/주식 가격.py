def solution(prices):
    answer = []
    temp = [0]*len(prices)
    for i in range(0, len(prices)):
        for j in range(i+1, len(prices)):
            if prices[i]<=prices[j]:
                temp[i] +=1
    answer = temp
    return answer

print(solution([1,2,3,2,3]))