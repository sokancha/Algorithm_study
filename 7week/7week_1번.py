'''
https://school.programmers.co.kr/learn/courses/30/lessons/155652
'''

def solution(s, skip, index):
    answer = ''
    alphabet = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'
    alphabet_list = []
    for i in range(len(alphabet)):
        alphabet_list.append(alphabet[i])

    for _ in range(3):
        for i in range(len(skip)):
            if skip[i] in alphabet_list:
                alphabet_list.remove(skip[i])

    for i in range(len(s)):
        for j in range(len(alphabet_list)):
            if s[i] == alphabet_list[j]:
                answer += alphabet_list[j + index]
                break

    return answer

print(solution("aukks","wbqd",	5))