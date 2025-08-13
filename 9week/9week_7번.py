'''
https://school.programmers.co.kr/learn/courses/30/lessons/42888
'''
def solution(record):
    answer = []
    list = []
    for i in record:
        list.append(i.split(" "))

    people = []
    for i in range(len(list)):
        if list[i][0] == 'Enter':
            people.append('enter')
            people.append(list[i][1])
        elif list[i][0] == 'Leave':
            people.append('leave')
            people.append(list[i][1])
        elif list[i][0] == 'Change':
            people.append('change')
            people.append(list[i][1])




    print(people)
    return answer


