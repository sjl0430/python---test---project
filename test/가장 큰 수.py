def solution(numbers):
    answer = ''
    arr = []
    num = []
    for i in numbers:
        arr += [str(i)+str(i)+str(i)]
        
    arr = sorted(arr,reverse = True)
    
    for i in arr:
           num += [i[:int(len(i) / 3)]]
           
    answer = ''.join(num)
    if set(numbers) =={0}:
        answer = '0'
    return answer

# 2 -> 3
# 111 11 10 110 100
# 111 11 110 1 101 10 100 1000 00
# 111 11 1 110 101 10 100 1000 00
# 110110110
# 111
# 100010001000
# 100100100