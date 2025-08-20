'''
https://school.programmers.co.kr/learn/courses/30/lessons/12982?language=python3
'''


def solution(d, budget):
    answer = 0
    d.sort()
    sum = 0
    for i in range(len(d)):
        if sum + d[i] <= budget:
            sum += d[i]
            answer += 1
        if sum + d[i] > budget:
            break

    return answer

print(solution([1,3,2,5,4],9))
print(solution([2,2,3,3],10))