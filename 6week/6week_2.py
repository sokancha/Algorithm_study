'''
https://school.programmers.co.kr/learn/courses/30/lessons/120847
정수 배열 numbers가 매개변수로 주어집니다.
umbers의 원소 중 두 개를 곱해 만들 수 있는
최댓값을 return하도록 solution 함수를 완성해주세요.

제한사항
0 ≤ numbers의 원소 ≤ 10,000
2 ≤ numbers의 길이 ≤ 100

numbers	                    result
[1, 2, 3, 4, 5]	            20
[0, 31, 24, 10, 1, 9]	    744
'''

def solution(numbers):
    answer = 0
    x = []
    for i in range(len(numbers)):
        for j in numbers[i + 1:]:
            multiply = numbers[i] * j
            x.append(multiply)

    answer = x[0]
    for m in range(1, len(x)):
        if x[m] > answer:
            answer = x[m]

    return answer

print(solution([1, 2, 3, 4, 5]))
print(solution([0, 31, 24, 10, 1, 9]))
