def solution(distance, rocks, n):
    answer = 0
    stone = list(set(rocks+[0]))
    # 보류
    rock = dict(zip(stone, stone[1:]))
    print(rock)

    return answer

print(solution(25, [2, 14, 11, 21, 17], 2))