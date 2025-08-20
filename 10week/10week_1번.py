'''
https://school.programmers.co.kr/learn/courses/30/lessons/120907
'''

def solution(quiz):
    answer = []
    for i in range(len(quiz)) :
        equal = quiz[i].index('=')      #quiz의 "="의 인덱스위치 찾기
        if eval(quiz[i][:equal]) == int(quiz[i][equal+2:]) :    # eval은 문자열로된 식을 계산하는 함수
                   answer.append("O")
        else :
                   answer.append("X")
    return answer

print(solution(["3 - 4 = -3", "5 + 6 = 11"]))
print(solution(["19 - 6 = 13", "5 + 66 = 71", "5 - 15 = 63", "3 - 1 = 2"]	))