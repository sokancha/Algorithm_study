'''
https://school.programmers.co.kr/learn/courses/30/lessons/159994
'''


def solution(cards1, cards2, goal):
    answer = ''
    sum = 0
    index = 0
    if cards1[0] == goal[0]:
        while answer != 'No':
            for i in range(len(cards1)):  # cards1부터 돌림
                if cards1[i] == goal[index]:
                    sum += 1  # 맞으면 sum +=1
                    index += 1  # index는 goal의 단어맞췄으니 다음단어로 가기위해 카운팅변수임
                elif cards1[i] != goal[index] and i > 0:  # 다음거가 goal이랑 안맞을때 i>0 -> 다음거를 말하는거임
                    del cards1[:i]
                    break
                else:  # 애초부터 안맞으면
                    answer = 'No'  # 답없으니 No
                    break
            if sum == len(goal):  # sum값이 goal길이랑 같아지면 즉, 다 맞춰지면
                answer = 'Yes'
                break

            for j in range(len(cards2)):
                if cards2[j] == goal[index]:
                    sum += 1
                    index += 1
                elif cards2[j] != goal[index] and j > 0:
                    del cards2[:j]
                    break
                else:
                    answer = 'No'
                    break
            if sum == len(goal):
                answer = 'Yes'
                break

    elif cards2[0] == goal[0]:
        while answer != 'No':
            for j in range(len(cards2)):
                if cards2[j] == goal[index]:
                    sum += 1
                    index += 1
                elif cards2[j] != goal[index] and j > 0:
                    del cards2[:j]
                    break
                else:
                    answer = 'No'
                    break

            if sum == len(goal):
                answer = 'Yes'
                break

            for i in range(len(cards1)):
                if cards1[i] == goal[index]:
                    sum += 1
                    index += 1
                elif cards1[i] != goal[index] and i > 0:
                    del cards1[:i]
                    break
                else:
                    answer = 'No'
                    break

            if sum == len(goal):
                answer = 'Yes'
                break

    return answer

print(solution(["i", "drink", "water"],["want", "to"],["i", "want", "to", "drink", "water"]))
print(solution(["i", "water", "drink"],["want", "to"],["i", "want", "to", "drink", "water"]))