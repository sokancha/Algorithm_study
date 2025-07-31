'''
https://school.programmers.co.kr/learn/courses/30/lessons/12981
'''

def solution(n, words):
    answer = []
    s = []
    i = 1
    s.append(words[0])

    while words[i][0] == words[i - 1][-1] and not words[i] in s:
        s.append(words[i])
        i += 1
        if i == len(words) :
            break
        if len(s) == len(words) :
            break

    if len(s) != len(words) :
        answer.append(len(s) % n + 1)
        answer.append(len(s) // n + 1)
    else :
        answer.append(0)
        answer.append(0)

    return answer

print(solution(3,["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]))
print(solution(5,["hello", "observe", "effect", "take", "either", "recognize", "encourage", "ensure", "establish", "hang", "gather", "refer", "reference", "estimate", "executive"]))
print(solution(2,["hello", "one", "even", "never", "now", "world", "draw"]))