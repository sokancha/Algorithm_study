'''
정수 배열 numbers와 정수 num1, num2가 매개변수로 주어질 때,
numbers의 num1번 째 인덱스부터 num2번째 인덱스까지 자른 정수 배열을 return 하도록 solution 함수를 완성해보세요.

numbers	        num1	    num2	    result
[1, 2, 3, 4, 5]	1	        3	        [2, 3, 4]
[1, 3, 5]	    1	        2	        [3, 5]
'''


def solution(numbers, num1, num2):
    answer = []
    for i in numbers[num1:num2 + 1]:
        answer.append(i)

    return answer

print(solution([1, 2, 3, 4, 5],1,3,))
print(solution([1, 3, 5],1,2,))