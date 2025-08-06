'''
https://school.programmers.co.kr/learn/courses/30/lessons/181852
'''


def solution(num_list):
    answer = []
    num_list.sort()

    for i in num_list[0:5]:
        num_list.remove(i)

    answer = num_list
    return answer