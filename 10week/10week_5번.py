'''
https://school.programmers.co.kr/learn/courses/30/lessons/12935
'''
def solution(arr):
    answer = []
    if len(arr) == 1:
        answer.append(-1)
    else :
        s = arr[0]
        for i in arr :
            if s >= i :
                s = i
                print(s)
        arr.remove(s)
        answer = arr
    return answer

print(solution([4,3,2,1]))
print(solution([10]))