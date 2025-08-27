'''
https://school.programmers.co.kr/learn/courses/30/lessons/181851
'''


def solution(rank, attendance):
    answer = 0
    rank_list = [None] * len(rank)  # 학생등수를 기준으로 번호순으로 넣을 리스트
    for i in range(len(rank)):
        a = rank.index(rank[i])
        rank_list[rank[i] - 1] = a  # 해당 등수에 맞게 인덱스 지정하여 넣어줌.

    # 그랬을때 rank_list는 첫번째 입출력예시 기준 [6,2,0,4,3,5,1] 이렇게 됨.

    num = 0  # 대회에 선발된 학생 중 등수순서
    for i in rank_list:
        if attendance[i] == True:
            if num == 0:  # 첫번째 순서 X10000
                answer += 10000 * i
                num += 1
            elif num == 1:
                answer += 100 * i
                num += 1
            elif num == 2:
                answer += i
                num += 1
            if num == 3:
                break
    return answer

print(solution([3, 7, 2, 5, 4, 6, 1],[False, True, True, True, True, False, False]))
print(solution([1, 2, 3],[True, True, True]))
print(solution([6, 1, 5, 2, 3, 4],[True, False, True, False, False, True]))
