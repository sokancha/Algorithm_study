'''
https://school.programmers.co.kr/learn/courses/30/lessons/250121
'''


def solution(data, ext, val_ext, sort_by):
    answer = [[]]
    list = []
    if ext == 'code':  # 상황에 맞게 분류
        for i in range(len(data)):
            if data[i][0] < val_ext:  # 비교
                list.append(data[i])  # 리스트에 넣어줌
    elif ext == 'date':
        for i in range(len(data)):
            if data[i][1] < val_ext:
                list.append(data[i])
    elif ext == 'maximum':
        for i in range(len(data)):
            if data[i][2] < val_ext:
                list.append(data[i])
    elif ext == 'remain':
        for i in range(len(data)):
            if data[i][3] < val_ext:
                list.append(data[i])

    # list = [[1,20300104,100,80],[3,20300401,10,8]]

    if sort_by == 'code':
        answer = sorted(list, key=lambda x: x[0])
    if sort_by == 'date':
        answer = sorted(list, key=lambda x: x[1])
    if sort_by == 'maximum':
        answer = sorted(list, key=lambda x: x[2])
    if sort_by == 'remain':
        answer = sorted(list, key=lambda x: x[3])
    # key는 정렬기준을 지정하는 매개변수, x는 list에서 하나씩 받아와서 x[]를 반환함. 반환한 값을 기준으로 sorted정렬
    return answer

print(solution([[1, 20300104, 100, 80], [2, 20300804, 847, 37], [3, 20300401, 10, 8]],"date",20300501,"remain"))
