'''
https://school.programmers.co.kr/learn/courses/30/lessons/12948
'''


def solution(phone_number):
    answer = ''
    num = 0
    for i in phone_number[::-1]:
        if num < 4:
            answer += i
        elif num >= 4:
            answer += "*"
        num += 1

    answer = answer[::-1]
    return answer

print(solution("01033334444"))
print(solution("027778888"))