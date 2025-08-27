'''
https://school.programmers.co.kr/learn/courses/30/lessons/68644
'''


def solution(numbers):
    from itertools import combinations
    answer = []
    com = list(combinations(numbers, 2))  # combinations는 조합을 만들어줌. 예를 들어 (2,1),(2,3)이렇게

    l = []
    for i in com:
        l.append(i[0] + i[1])

    for j in set(l):
        answer.append(j)
    answer.sort()

    return answer

print(solution([2,1,3,4,1]))
print(solution([5,0,2,7]))