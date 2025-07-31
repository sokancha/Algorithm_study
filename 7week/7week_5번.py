'''
https://school.programmers.co.kr/learn/courses/30/lessons/118666
'''


def solution(survey, choices):
    answer = ''
    list = []
    for i in range(len(survey)):
        if choices[i] > 4:
            for j in range(choices[i] - 4):
                list.append(survey[i][1])
        elif choices[i] < 4:
            for j in range(4 - choices[i]):
                list.append(survey[i][0])
        else:
            continue

    arr = {'R': 0, 'T': 0, 'C': 0, 'F': 0, 'J': 0, 'M': 0, 'A': 0, 'N': 0}

    for i in list:
        for key, value in arr.items():
            if i in arr:
                arr[i] += 1
                break

    if arr['R'] >= arr['T']:
        answer += 'R'
    else:
        answer += 'T'
    if arr['C'] >= arr['F']:
        answer += 'C'
    else:
        answer += 'F'
    if arr['J'] >= arr['M']:
        answer += 'J'
    else:
        answer += 'M'
    if arr['A'] >= arr['N']:
        answer += 'A'
    else:
        answer += 'N'

    return answer

print(solution(["AN", "CF", "MJ", "RT", "NA"],[5, 3, 2, 7, 5]))
print(solution(["TR", "RT", "TR"],[7, 1, 3]))