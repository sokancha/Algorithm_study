'''
https://school.programmers.co.kr/learn/courses/30/lessons/120904
'''
def solution(num, k):
    answer = 0

    def seq_search(a, key):
        i = 0
        while True:
            if i == len(a):
                return -1
            if a[i] == key:
                return i+1
            i += 1

    num_list = []
    str_key = str(k)
    str_num = str(num)
    for i in range(len(str_num)):
        num_list.append(str_num[i])

    answer = seq_search(str_num, str_key)
    return answer

print(solution(29183,1))
print(solution(232443,4))
print(solution(123456,7))