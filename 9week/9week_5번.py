"""
https://school.programmers.co.kr/learn/courses/30/lessons/87390
"""


def solution(n, left, right):  # 리스트 둘다 만들어주고 시작
    answer = [None] * (right - left + 1)  # 정답에 들어갈 리스트
    list = [None] * n ** 2  # 이건 기본 리스트
    index = 0  # 기본 리스트에서 사용할 인덱스 카운팅변수

    for a in range(1, n + 1):  # 기본 리스트에 하나씩 값 추가
        for _ in range(1, a + 1):
            list[index] = a
            index += 1  # 인덱스 값 늘려주면서
        for b in range(a, n):
            list[index] = b + 1
            index += 1

    i = 0  # 정답리스트에서 사용할 카운팅변수
    for c in list[left:right + 1]:  # 구간 반복
        answer[i] = c  # 리스트에 추가
        i += 1

    return answer


print(solution(3,2,5))
print(solution(4,7,14))