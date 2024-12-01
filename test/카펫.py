def solution(brown, yellow):
    answer = []
    n = 0
    while True:
        n += 1
        y_row = yellow / n 
        y_col = n
        if brown + yellow == (y_row + 2) * (y_col + 2):
            break
    answer+= [int(y_row + 2), y_col + 2]
    return answer
