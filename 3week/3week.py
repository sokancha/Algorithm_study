#실습 1-7
# 1부터 n까지 정수의 합 구하기 1 (while문)
'''
print('1부터 n까지 정수의 합을 구합니다.')
n = int(input('n값을 입력하세요. :'))

sum = 0
i = 1

while i <= n :
    sum += i
    i += 1

print(f'1부터 {n}까지 정수의 합은 {sum}입니다.')


#실습 1-8
#1부터 n까지의 정수의 합 구하기 2(for문)

print('1부터 n까지 정수의 합을 구합니다.')
n = int(input('n값을 입력하세요. :'))

sum = 0
for i in range(1, n+1) :
    sum += i #sum에 i를 더함

print(f'1부터 {n}까지 정수의 합은 {sum}입니다.')

#p34 조금만더

print('1부터 n까지 정수의 합을 구합니다.')
n = int(input('n값을 입력하세요. :'))

sum = n * (n+1) // 2

print(sum)


#실습 1-9
#a부터 b까지 정수의 합 구하기(for문)

print('a부터 b까지 정수의 합을 구합니다.')
a = int(input('정수 a를 입력하세요. :'))
b = int(input('정수 b를 입력하세요. :'))

if a > b :
    a,b = b,a # a와 b를 오름차순으로 정렬

sum = 0
for i in range(a,b+1) :
    sum += i # sum에 i를 더함

print(f'{a}부터 {b}까지 정수의 합은 {sum}입니다.')


#실습 1-10
#a부터 b까지 정수의 합 구하기 1

print('a부터 b까지 정수의 합을 구합니다.')
a = int(input('정수 a를 입력하세요. :'))
b = int(input('정수 b를 입력하세요. :'))

if a > b :
    a, b = b, a

sum = 0
for i in range(a, b+1) :
    if i < b :
        print(f'{i}+ ', end = '') # i가 b보다 작으면 합을 구하는 과정 출력
    else :
        print(f'{i} =', end = '') # i가 b보다 크거나 같으면 최종값 출력을 위해 i =를 출력
    sum += i

print(sum)


#실습 1-11
#a부터 b까지 정수의 합 구하기 2

print('a부터 b까지 정수의 합을 구합니다.')
a = int(input('정수 a를 입력하세요. :'))
b = int(input('정수 b를 입력하세요. :'))

if a > b :
    a,b = b,a

sum = 0
for i in range(a, b) :
    print(f' {i} +', end = '')
    sum += i # sum에 i를 더함

print(f' {b} = ', end = '')
sum += b

print(sum)


#실습1-12
#+와 -를 번갈아 출력하기 1


print('+와 -를 번갈아 출력합니다.')
n = int(input('몇 개를 출력할까요? :'))

for i in range(n) :

    if i % 2 :
        print('-', end= '')
    else :
        print('+', end= '')

print()


# +와 -를 번갈아 출력하기 1(for문 수정)

print('+와 -를 번갈아 출력합니다.')
n = int(input('몇 개를 출력할까요? :'))

for i in range(1, n+1) :
    if i % 2 : #홀수
        print('+', end='')
    else :
        print('-', end='')

print()


#실습1-13
#+와 -를 번갈아 출력하기 2

print('+와 -를 번갈아 출력합니다.')
n = int(input('몇 개를 출력할까요? :'))

for _ in range(n // 2) :
    print('+=', end='')
if n % 2 :
    print('+', end='')

print()

#*를 n // w번 출력하기
n = int(input('*의 개수 :'))
w = int(input('한묶음의 몇개 :'))
print(f'{n}개의 별을 {w}개로 묶어서 출력합니다.')

for _ in range( n // w ) :
    for i in range(w) :
        print('*', end ='')
    print(' ', end= '')

print()


print('*를 출력합니다.')
n = int(input('몇 개를 출력할까요? :'))

for _ in range(n // 5) :
    print('*****', end = '')
if n % 5 :
    i = n % 5
    for _ in range(i) :
        print('*', end = '')

print()



#*를 n % w번 출력 후 줄바꿈하기

n = int(input('*의 총 개수 :'))
w = int(input('한 묶음의 개수 :'))
print(f'{n}개의 *를 {w}개로 나눈 개수만큼 출력 후 줄바꿈합니다.')


for _ in range(n // w) :
    for i in range(w) :
        print('*', end='')
    print('\n', end='')
for a in range(n%w) :
    print('*', end='')

print()


#실습 1-16
# 1부터 n까지 정수의 합 구하기(n값은 양수만 입력받음)

print('1부터 n까지 정수의 합을 구합니다.')

while True :
    n = int(input('n값을 입력하세요. :'))
    if n > 0 :
        break #n이 0보다 커질 때까지 반복

sum = 0
i = 1

for i in range(1, n+1) :
    sum += i
    i += 1

print(f'1부터 {n}까지 정수의 합은 {sum}입니다.')

'''
