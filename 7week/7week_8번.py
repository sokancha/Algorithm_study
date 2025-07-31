'''
https://school.programmers.co.kr/learn/courses/30/lessons/87390
'''


def solution(n, left, right):
    answer = [None] * (right - left + 1)
    list = [None] * n ** 2
    index = 0

    for a in range(1, n + 1):
        for _ in range(1, a + 1):
            list[index] = a
            index += 1
        for b in range(a, n):
            list[index] = b + 1
            index += 1

    i = 0
    for c in list[left:right + 1]:
        answer[i] = c
        i += 1

    return answer

