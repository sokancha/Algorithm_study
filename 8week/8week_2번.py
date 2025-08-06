'''
https://school.programmers.co.kr/learn/courses/30/lessons/17677
'''

def solution(str1, str2):
    import copy

    answer = 0
    list_str1 = []
    list_str2 = []
    list_hap1 = []
    list_hap2 = []
    str1 = str1.lower()
    str2 = str2.lower()

    so = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

    for i in range(len(str1)-1):
        if str1[i:i+2][0] in so and str1[i:i+2][1] in so :
            list_str1.append(str1[i:i + 2])
    list_hap1 = copy.deepcopy(list_str1)

    for i in range(len(str2)-1):
        if str2[i:i + 2][0] in so and str2[i:i + 2][1] in so:
            list_str2.append(str2[i:i + 2])
    list_hap2 = copy.deepcopy(list_str2)

    #교집합
    sum = 0
    for i in list_str1 :
        for j in list_str2 :
            if i in j :
                sum += 1
                list_str2.remove(j)
                break

    #합집합
    hap = 0
    for i in list_hap1 :
        hap += 1
        for j in range(len(list_hap2)) :
            if i == list_hap2[j] :
                list_hap2.pop(j)
                break



    hap += len(list_hap2)

    if hap == 0 and sum == 0 :
        answer = 65536
    else :
        k = sum/hap
        answer = int(65536*k)

    return answer

print(solution('FRANCE','french'))
print(solution('handshake','shake hands'))
print(solution('aa1+aa2','AAAA12'))
print(solution('E=M*C^2','e=m*c^2'))