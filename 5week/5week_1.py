'''
정수를 담고 있는 배열 arr의 평균값을 return하는 함수, solution을 완성해보세요.

arr	        return
[1,2,3,4]	2.5
[5,5]	    5


'''

def solution(arr):
    answer = 0
    for i in arr :
        answer += i
    answer = answer/len(arr)
    return answer

print(solution([1,2,3,4]))
print(solution([5,5]))