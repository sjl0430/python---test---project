def solution(n):
    def resol(m, start, temp, target):
        if m == 1:
            return [[start, target]]
        op = resol(m-1, start, target, temp)
        mid = [[start, target]]
        fin = resol(m-1, temp, start, target)
        return op + mid + fin
    
    return resol(n, 1, 2, 3)


# print(solution(3))


