"""
https://school.programmers.co.kr/learn/courses/30/lessons/42862
"""

def solution(n, lost, reserve):
    answer = 0
    k = [] #여벌이 있는 사람중에서 이미 빌려준사람
    for i in range(n) :
        if not i in reserve and not i in lost :
            answer += 1
        elif i in reserve :
            answer += 1
        elif i in lost :
            if i+1 in reserve :
                if not i+1 in k :
                    answer += 1
                    k.append(i+1)
            elif i-1 in reserve :
                if not i-1 in k :
                    answer += 1
                    k.append(i-1)
    return answer