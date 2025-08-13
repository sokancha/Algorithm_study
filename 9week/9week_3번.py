'''
https://school.programmers.co.kr/learn/courses/30/lessons/120861
'''

def solution(keyinput, board):
    answer = [0,0]
    for i in keyinput :
        if i == 'left' :
            if answer[0] > -(board[0]//2) :
                answer[0] = answer[0] - 1
        if i == 'right' :
            if answer[0] < board[0]//2 :
                answer[0] = answer[0] + 1
        if i == 'up' :
            if answer[1] < board[1]//2 :
                answer[1] = answer[1] + 1
        if i == 'down' :
            if answer[1] > -(board[1]//2) :
                answer[1] = answer[1] - 1
    return answer

print(solution(["left", "right", "up", "right", "right"]))
print(solution(["down", "down", "down", "down", "down"]))