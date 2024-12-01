def solution(answers):
    answer = []
    s1 = no_1(answers)
    s2 = no_2(answers)
    s3 = no_3(answers)
    
    if s1 == s2:
        if s2 == s3:
            answer += [1,2,3]
        elif s1 > s3:
            answer += [1,2]
    elif s1 > s2 and s1 > s3:
        answer.append(1)
    elif s2 == s3 and s1 < s2:
        answer += [2,3]
    elif s2 > s3 and s1 < s2:
        answer.append(2)
    elif s3 == s1 and s2 < s3:
        answer += [1,3]
    elif s3 > s1 and s3 > s2:
        answer.append(3)
    
    return answer



def no_1(answers):
    score = 0
    for i in range(len(answers)):
        if answers[i] % 5 == (i+1) % 5:
            score += 1
            
    return score
    
def no_2(answers):
    score = 0
    for i in range(len(answers)):
        if i % 2 == 0 and answers[i]==2:
            score += 1
        elif i % 8 == 1 and answers[i] == 1:
            score += 1
        elif i % 8 == 3 and answers[i] == 3:
            score += 1
        elif i % 8 == 5 and answers[i] == 4:
            score += 1
        elif i % 8 == 7 and answers[i] == 5:
            score += 1
    
    return score

def no_3(answers):
    score = 0
    for i in range(len(answers)):
        if i % 10 == 0 or i % 10 == 1:     
            if answers[i] == 3:
                score += 1
        elif i % 10 == 2 or i % 10 == 3:
            if answers[i] == 1:
                score += 1
        elif i % 10 == 4 or i % 10 == 5:
            if answers[i] == 2:
                score += 1
        elif i % 10 == 6 or i % 10 == 7:
            if answers[i] == 4:
                score += 1
        elif i % 10 == 8 or i % 10 == 9:
            if answers[i] == 5:
                score += 1
            
    return score
