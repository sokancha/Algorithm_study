'''
https://school.programmers.co.kr/learn/courses/30/lessons/12924
'''


def solution(n):
    answer = 0
    list = [None] * n
    for i in range(n):
        list[i] = i + 1

    for j in range(len(list)):
        k = 0
        for a in list[j:]:
            k += a
            if k >= n:
                if k == n:
                    answer += 1
                else:
                    break
    return answer