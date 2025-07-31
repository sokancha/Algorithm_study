'''
https://school.programmers.co.kr/learn/courses/30/lessons/92335
'''
ptr = 0
for k in range(3,11) :
    n = 437674
    answer = 0
    sum = []
    m = ''
    dchar = '0123456789ABCDEF'

    while n > 0:
        m += dchar[n % k]
        n //= k

    m = m[::-1]

    print(m)


    # 0P0이 되는 조건
    for i in range(len(m)):
        if '0' in m[i+2:-2] and m[i] == '0':
            if m[i + 1] != '0' and '0' in m[i + 2:]:
                d = 0
                for j in m[i+2:] :
                    if j == '0' :
                        sum.append(m[i+1:i+d+2])
                        break
                    d += 1
        if len(m[i:]) == 2:
            break

    # P0이 되는 조건
    for i in range(len(m)):
        if m[i] == '0':
            sum.append(m[:i])
            break

    # 0P가 되는 조건
    k = 1
    for i in m[::-1]:
        if i == '0':
            sum.append(m[-k + 1:])
            break

        k += 1

    plus = 0
    for i in m:
        if i != '0':
            plus += 1
        if plus == len(m):
            sum.append(m)
    print(sum)

    for a in range(len(sum)):
        if '2' in sum:
            answer += 1
            sum.remove('2')
        if '3' in sum:
            answer += 1
            sum.remove('3')
        if '1' in sum:
            sum.remove('1')

    for a in range(len(sum)):
        for b in range(2, int(sum[a])):
            if int(sum[a]) % b == 0:
                break
        else:
            answer += 1

    ptr += 1
    print(f'{ptr+2}진법 {answer}')



