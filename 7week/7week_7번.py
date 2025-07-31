'''
https://school.programmers.co.kr/learn/courses/30/lessons/155651


def solution(book_time):
    answer = 0
    for i in book_time :
        if int(book_time[i][1].split(":")[0]) < int(book_time[i+1][0].split(":")[0]) :
            answer += 1
            return answer
        elif int(book_time[i][1].split(":")[0]) == int(book_time[i+1][0].split(":")[0]) :
            if int(book_time[i][1].split(":")[1]) + 10 < int(book_time[i+1][0].split(":")[1]) :
                answer += 1
                return answer
    return answer
'''


def solution(book_time):
    answer = 0
    list = []
    for i in book_time:
        sublist = []
        for j in i:
            front = int(j.split(':')[0]) * 60
            back = int(j.split(':')[1])
            sublist.append(front + back)

        list.append(sublist)

    print(list)

    for a in list[:-1] :
        k = 0
        for b in list[k+1:] :
            if a[0] < b[0] :
                if a[1] + 10 <= b[0] :
                    continue
                else :
                    answer += 1
            elif a[0] > b[0] :
                if b[1] + 10 <= a[0] :
                    continue
                else :
                    answer += 1
            else :
                answer += 1

        if answer == len(book_time):
            break

    return answer

print(solution([["15:00", "17:00"], ["16:40", "18:20"], ["14:20", "15:20"], ["14:10", "19:20"], ["18:20", "21:20"]]))

'''
def solution(book_time):
    answer = 0
    list = []
    for i in book_time:
        sublist = []
        for j in i:
            a = j.split(':')[0]
            b = j.split(':')[1]
            sublist.append(int(a + b))

        list.append(sublist)

    for a in range(len(list)):
        for b in list[a + 1:]:
            if list[a][0] < b[0]:
                if list[a][1] + 10 <= b[0]:
                    answer += 1
            elif list[a][0] > b[0]:
                if b[1] + 10 < list[a][0]:
                    answer += 1
            else:
                answer += 1

        if answer == len(book_time):
            break

    return answer

'''