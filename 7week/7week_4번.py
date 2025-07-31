'''
https://school.programmers.co.kr/learn/courses/30/lessons/17681
'''

def solution(n, arr1, arr2):
    answer = []
    list1 = []
    list2 = []

    for i in arr1:
        d = ''
        dchar = '01'
        while i > 0:
            d += dchar[i % 2]
            i //= 2
        if len(d) < n:
            for _ in range(n - len(d)):
                d += '0'
        list1.append(d[::-1])
    print(list1)

    for i in arr2:
        d = ''
        dchar = '01'
        while i > 0:
            d += dchar[i % 2]
            i //= 2
        if len(d) < n:
            for _ in range(n - len(d)):
                d += '0'
        list2.append(d[::-1])
    print(list2)

    num = 0
    for a in list1:
        sum = ''
        for i in range(n):
            if a[i] == '0' and list2[num][i] == '0' :
                sum += " "
            else:
                sum += "#"
        print(sum)
        answer.append(sum)
        num += 1

    return answer

print(solution(5,[9, 20, 28, 18, 11],[30, 1, 21, 17, 28]))
print(solution(6,[46, 33, 33 ,22, 31, 50],[27 ,56, 19, 14, 14, 10]))