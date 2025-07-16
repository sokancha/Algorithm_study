#실습 1-16
#1부터 n까지 정수의 합 구하기(n값은 양수만 입력 받음)
'''
print('1부터 n까지 정수의 합을 구합니다.')

while Ture :
    n = int(input('n값을 입력하세요.:')
    if n > 0 :
        break ; #n이 0보다 커질 때까지 반복

sum = 0
i = 1

for i in range(1, n+1):
    sum += i
    i += 1

print(f'1부터 {n}까지 정수의 합은 {sum}입니다.')


#실습 1-17
#가로,세로 길이가 정수이고, 넓이가 area인 직사각형에서 변의 길이 나열하기

area = int(input('직사각형의 넓이를 입력하세요.:'))

for i in range(1, area+1) :
    if i * i > area: break
    if area % i : continue
    print(f'{i} x {area // i}')


#실습 1-18
#10~99 사이의 난수 n개 생성하기(13이 나오면 중단)

import random

n = int(input('난수의 개수를 입력하세요. :'))

for _ in range(n) :
    r = random.randint(10,99)
    print(r,end= ' ')
    if r == 13:
        print('\n프로그램을 중단합니다.')
        break
else :
    print('\n난수 생성을 종료합니다.')


#실습 1-19
# 1~12까지 8을 건너뛰고 출력하기 1

for i in range(1,13) :
    if i == 8 :
        continue
    print(i, end=' ')

print()

#실습 1-20
#1부터 12까지 8을 건너뛰고 출력하기 2

for i in list(range(1,8)) +list(range(9,13)) :
    print(i, end=' ')
print()

#실습1C-3
#2자리 양수(10~99) 입력받기

print('2자리 양수를 입력하세요 :')

while True :
    no = int(input('값을 입력하세요:'))
    if no >= 10 and no <= 99 :
        break
print(f'입력받은 양수는 {no}입니다.')


#실습 1-21
#구구단 곱셈표 출력하기

print('-' * 27)
for i in range(1, 10) :
    for j in range(1, 10) :
        print(f'{i * j:3}', end='')
    print() #행 변경
print('-' * 27)


#실습1-22
#왼쪽 아래가 직각인 이등변 삼각형으로 * 출력하기

print('왼쪽 아래가 직각인 이등변 삼각형을 출력합니다.')
n = int(input('짧은 변의 길이를 입력하세요.:'))

for i in range(n) :
    for j in range(i+1) :
        print('*', end='')
    print() #행 변경

#실습1-23
#오른쪽 아래가 직각인 이등변 삼각형으로 * 출력하기

print('오른쪽 아래가 직각인 이등변 삼각형을 출력합니다.')
n = int(input('짧은 변의 길이를 입력하세요. :'))

for i in range(n) :
    for _ in range(n-i-1) :
        print(' ', end='')
    for _ in range(i+1) :
        print('*', end='')
    print()

#실습 1C-4
#함수 내부,외부에서 정의한 변수와 객체의 식별 번호를 출력하기

n= 1 #전역 변수(함수 내부,외부에서 사용)
def put_id() :
    x = 1
    print(f'id(x) = {id(x)}')

print(f'id(1) = {id(1)}')
print(f'id(n) = {id(n)}')
put_id()

#실습1C-5
#1부터 100까지 반복하여 출력하기
for i in range(1,101) :
    print(f'i ={i:3}   id(i) = {id(i)}')


'''
