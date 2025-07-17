'''
def solution(n):
    answer = 0
    n = str(n)
    for i in range(len(n)) :
        answer += int(n[i])
    return answer
'''

'''
https://school.programmers.co.kr/learn/courses/30/lessons/12931
자릿수 더하기

문제 설명 : 자연수 N이 주어지면, 
N의 각 자릿수의 합을 구해서 return 하는 solution 함수를 만들어 주세요.
예를들어 N = 123이면 1 + 2 + 3 = 6을 return 하면 됩니다.

입출력 예:
N	answer
123	6
987	24

'''

def solution(n):
    answer = 0
    i = 0
    n = str(n)
    while True :
        answer += int(n[i])
        i += 1
        if i == len(n) :
            break

    return answer

print(solution(123))
print(solution(987))