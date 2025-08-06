'''
https://school.programmers.co.kr/learn/courses/30/lessons/134240
'''


def solution(food):
    import copy
    answer = ''
    answer_copy = ''

    for i in range(len(food)):
        if food[i] >= 2 and food[i] <= 3:
            answer += str(i)
        elif food[i] > 3:
            answer += str(i) * (food[i] // 2)

    answer_copy = copy.deepcopy(answer)
    answer_copy = answer_copy[::-1]
    answer += '0'
    answer += answer_copy

    return answer

print(solution([1,3,4,6]))
print(solution([1, 7, 1, 2]))