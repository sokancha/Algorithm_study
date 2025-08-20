'''
https://school.programmers.co.kr/learn/courses/30/lessons/12916
'''

def solution(s):
    answer = True
    p_sum = 0
    y_sum = 0
    for i in s :
        if i == 'P' or i == 'p' :
            p_sum += 1
        if i == 'Y' or i == 'y' :
            y_sum += 1
    if p_sum == y_sum :
        answer = True
    if p_sum == 0 and y_sum == 0 :
        answer = True
    if p_sum != y_sum :
        answer = False
    return answer

print(solution("pPoooyY"))
print(solution("Pyy"))