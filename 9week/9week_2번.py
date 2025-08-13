'''
https://school.programmers.co.kr/learn/courses/30/lessons/132265



def solution(topping):
    answer = 0
    # 토핑이 1개씩 나눠질때
    for a in range(len(topping)):
        if len(set(topping[:a + 1])) == 1:
            if len(set(topping[a + 1:])) == 1:
                answer += 1
        elif len(set(topping[:a + 1])) >= 2:
            break
    # 토핑이 2개씩 나눠질때
    for b in range(len(topping)):
        if len(topping[:b + 1]) >= 2:
            if len(set(topping[:b + 1])) == 2:
                if len(set(topping[b + 1:])) == 2:
                    answer += 1
            elif len(set(topping[:b + 1])) >= 3:
                break
    # 토핑이 3개씩 나눠질때
    for c in range(len(topping)):
        if len(topping[:c + 1]) >= 3:
            if len(set(topping[:c + 1])) == 3:
                if len(set(topping[c + 1:])) == 3:
                    answer += 1
            elif len(set(topping[:c + 1])) >= 4:
                break
    # 토핑이 4개씩 나눠질때
    for d in range(len(topping)):
        if len(topping[:d + 1]) >= 4:
            if len(set(topping[:d + 1])) == 4:
                if len(set(topping[d + 1:])) == 4:
                    answer += 1

    return answer

'''


def solution(topping):
    answer = 0
    for i in range(len(topping) - 1):
        if len(set(topping[:i + 1])) == len(set(topping[i + 1:])):
            answer += 1

    return answer

print(solution([1, 2, 1, 3, 1, 4, 1, 2,]))
print(solution([1, 2, 3, 1, 4]))