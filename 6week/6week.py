'''
def max(a) :
    maximum = a[0]
    for i in range(1, len(a)) :
        if a[i] > maximum :
            maximum = a[i]

from typing import Any, Sequence

def max_of(a: Sequence) -> Any :
    maximum = a[0]
    for i in range(1, len(a)) :
        if a[i] > maximum :
            maximum = a[i]
    return maximum

if __name__ == '__main__' :
    print('배열의 최댓값을 구합니다.')
    num = int(input('원소 수를 입력하세요. :'))
    x = [None] * num

    for i in range(num) :
        x[i] = int(input(f'x[{i}]값을 입력하세요. :'))

    print(f'최댓값은 {max_of(x)}입니다.')

# Any => 제약이 없는 임의의 자료형
# sequence => 시퀀스형을 의미. 또한 시퀀스형에는 리스트형,바이트 배열형, 문자열형 ,튜플형, 바이트열형이 있다.

# 변수 __name__은 __main__이다.
# 스크립트 프로그램이 임포트될 때 변수 __name__은 원래의 모듈 이름이다.



print('배열의 최댓값을 구합니다.')
print('주의 : "End"를 입력하면 종료합니다.')

number = 0
x = []

while True :
    s = input(f'x[{number}]값을 입력하세요. :')
    if s == 'END' :
        break
    x.append(int(s))
    number += 1

print(f'{number}개를 입력했습니다.')
print(f'최댓값은 {max_of(x)}입니다.')


def max(a) :
    maximum = a[0]
    for i in range(1, len(a)) :
        if a[i] > maximum :
            maximum = a[i]

from typing import Any, Sequence

def max_of(a: Sequence) -> Any :
    maximum = a[0]
    for i in range(1, len(a)) :
        if a[i] > maximum :
            maximum = a[i]
    return maximum

import random

print('난수의 최댓값을 구합니다.')
num = int(input('난수의 개수를 입력하세요.:'))
lo = int(input('난수의 최솟값을 입력하세요. :'))
hi = int(input('난수의 최댓값을 입력하세요. :'))
x = [None] * num

for i in range(num) :
    x[i] = random.randint(lo,hi)

print(f'{(x)}')
print(f'이 가운데 최댓값은 {max_of(x)}입니다.')

'''

#튜플, 문자열, 문자열 리스트의 최댓값 구하기

#실습 2-5
#각 배열 원소의 최댓값을 구해서 출력하기(튜플,문자열,문자열리스트)

def max(a) :
    maximum = a[0]
    for i in range(1, len(a)) :
        if a[i] > maximum :
            maximum = a[i]

from typing import Any, Sequence

def max_of(a: Sequence) -> Any :
    #sequence는 매개변수 a는 sequence타입이어야함. sequence는 list,tuple,str등 순서가 있는 컬렉션을 포함하는 추상베이스클래스이며, -> Any 이 함수는 어떤 타입이든 반환할 수 있다는 말이다. 만약 int만 반환한다면 -> int와 같이 더 구체적으로 명시할 수 있다.
    maximum = a[0]
    for i in range(1, len(a)) :
        if a[i] > maximum :
            maximum = a[i]
    return maximum

l = [1,2,3]
t = (4,7,5.6,2,3.14,1)
s = 'string'
a = ['DTS', 'AAC', 'FLAC']

print(f'{l}의 최댓값은 {max(l)}입니다.')
print(f'{t}의 최댓값은 {max_of(t)}입니다.')
print(f'{s}의 최댓값은 {max_of(s)}입니다.')
print(f'{a}의 최댓값은 {max_of(a)}입니다.')

'''
lst1 = [1,2,3,4,5]
lst2 = [1,2,3,4,5]

lst1 is lst2
>>> False

lst1 = [1,2,3,4,5]
lst2 = lst1
lst1 is lst2
>>> True
lst1[2] = 9
lst1
>>> [1,2,9,4,5]
lst2
>>> [1,2,9,4,5]
'''

#리스트 스캔

#실습 2C-1 : 원소 수를 len()함수로 미리 알아내서 0에서 원소수를 -1까지 반복한다.
x = ['Jhon','George','Paul','Ringo']

for i in range(len(x)) :
    print(f'x[{i}] = {x[i]}')

#실습 2C-2 : 인덱스와 원소를 짝지어 enumerate()함수로 반복해서꺼낸다.
#enumerate()함수는 인덱스와 원소를 짝지어 튜플로 꺼내는 내장 함수이다.
x = ['Jhon','George','Paul','Ringo']

for i, name in enumerate(x) :
    print(f'x[{i}] = {x[i]}')
#실습 2C-3 : 실습2C-2와 같지만 1부터 카운트를 시작한다.

x = ['Jhon','George','Paul','Ringo']

for i, name in enumerate(x, 1) :
    print(f'{i}번째 = {name}')

#실습 2C-4 : 인덱스값을 사용하지 않고 in을 사용해서 원소를 처음부터 순서대로 꺼낸다.
x = ['Jhon','George','Paul','Ringo']

for i in x :
    print(i)

#튜플의 스캔
x = ('John', 'George', 'Paul', 'Ringo')

#문자열, 리스트, 튜플, 집합, 딕셔너리 등의 자료형 객체는 모두 이터러블(반복 가능)하다는 공통점을 가지고 있다.
#이터러블 객체는 원소를 하나씩 꺼내는 구조이며, 이터러블 객체를 내장 함수인 iter()의 인수로 전달하면 그 객체에 대한 이터레이터(반복자)를 반환한다.
#이터레이터는 데이터의 나열을 표현하는 객체이다. 이터레이터의 __next__함수를 호출하거나 내장 함수인 next()함수에 이터레이터를 전달하면 원소를 순차적으로 꺼낼 수 있다. 꺼낼 원소가 더 이상 없는 경우 StopIteration으로 예외 발생을 시킨다.

#배열 원소를 역순으로 정렬하기

#실습 2-6
#뮤터블 시퀀스 원소를 역순으로 정렬

from typing import Any, MutableSequence

def reverse_array(a: MutableSequence) -> None :
    """뮤터블 시퀀스 a의 원소를 역순으로 정렬"""
    n = len(a)
    for i in range(n//2) :
        a[i], a[n-i-1] = a[n-i-1],a[i]

if __name__ == '__main__' :
    print('배열 원소를 역순으로 정렬합니다.')
    nx = int(input('원소 수를 입력하세요. :'))
    x = [None] * nx #원소 수가 nx인 리스트를 생성

    for i in range(nx) :
        x[i] = int(input(f'x[{i}]값을 입력하세요.:'))

    reverse_array(x)#x를 역순으로 정렬


    print('배열 원소를 역순으로 졍렬했습니다.')
    for i in range(nx) :
        print(f'x[{i}] = {x[i]}')

#reverse_array()함수를 호출하여 역순으로 정렬하고 그 원솟값을 출력하였다.

#리스트를 역순으로 정렬하기
#x.reverse()

y = list(reversed(x))

#16진수는 다음과 같이 문자 16개로 표현되는 수이다.
#0,1,2,3,4,5,6,7,8,9,A,B,C,D,E,F

#기수와 서수
#기수는 수를 타나태는 데 기초가 되며 10진법에서는 0~9까지 정수를 말한다.
#이 10개의 기수를 사용하여 무수히 많은 값을 수로 나타낼 수 있다.
#서수는 사물의 순서를 나타낸다.
#간단히 말해 기수는 1,2,3 ... 이고, 서수는 첫째, 둘째, 셋째, ...라고 생각하면 된다.

#10진수
#10진수는 다음과 같이 숫자 10종류를 사용하여 나타낸다.
#0 1 2 3 4 5 6 7 8 9

#10진수의 각 자리는 아랫자리부터 10^0, 10^1, 10^2 ... 으로 10의 거듭제곱값을 갖는다. 예를들어 1234는 다음과 같이 풀어 쓸 수 있다.
#1234 = 1 x 10^3 +2 x 10^2+ 3 x 10^1 + 4 x 10^0

#8진수는 다음과 같이 숫자 8종류를 사용하여 나타낸다.
#0 1 2 3 4 5 6 7

#1자릿수 : 0~7까지의 수를 나타낸다.
#2자릿수 : 10~77까지의 수를 나타낸다.
#3자릿수 : 100~777까지의 수를 나타낸다.
#ex) 5306 = 5 x 8^3 + 3 x 8^2 + 0 x 8^1 + 6 x 8^0

#16진수는 다음과 같이 숫자 16종류를 사용하여 나타낸다.
#0 1 2 3 4 5 6 7 8 9 A B C D E F

#0~F는 10진수로 0~15에 해당한다.(A~F는 소문자여도 상관없다.)
#ex) 12A0 = 1 x 16^3 + 2 x 16^2 + A x 16^1 + 0 x 16^0

#실습 2-7[A]
#10진수를 정숫값을 입력받아 2~36진수로 변환하여 출력하기
def card_conv(x:int, r:int) -> str:
    '''정숫값x를 r진수로 변환한 뒤 그 수를 나타내는 문자열을 반환'''

    d = ''
    dchar = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    while x > 0 :
        d += dchar[x%r] # 해당하는 문자를 꺼내 결합
        x //= r

    return d[::-1]

#card_conv()함수는 정수 x를 r진수로 변환하고 그 수를 문자열로 반환한다. 그리고 문자열 d를 빈 문자열로 초기화한다.
#그 뒤 while문의 루프 본문을 수행한다.
#238~239행에서는 x를 r로 나눈 나머지를 인덱스로 하는 문자, 곧 dchar[x%r]를 문자열 d에 추가한다.
#문자열 dchar에서는 '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'이 들어 있으므로 각 문자를 맨 앞부터 차례로 dchar[0],dchar[1]...dchar[35]로 접근할 수 있다.

#x가 0이 될 때까지 이 과정을 반복한다. 이때 x를 r로 나눈 나머지의 값 위치에 있는 문자를 d에 결합하므로 문자열 d의 맽 앞은 마지막으로 구한 문자가 된다. 따라서 반환된 문자열 d는 역순으로 출력해야한다.

#실습 2-7[B]
if __name__ == '__main__' :
    print('10진수를 n진수로 변환한다.')

    while True :
        while True : #음이 아닌 정수를 입력받음.
            no = int(input('변환할 값으로 음이 아닌 정수를 입력하세요. :'))
            if no > 0:
                break

        while True : #2~36진수의 정숫값을 입력받는다.
            cd = int(input('어떤 진수로 변환할까요? :'))
            if 2 <= cd <= 36 :
                break

        print(f'{cd}진수로는 {card_conv(no,cd)}입니다.')

        retry = input('한 번 더 변환할까요? (Y -- 예 / N -- 아니요) :')
        if retry in {'N', 'n'} :
             break

#256행에서 변환할 값 (음이 아닌 정수)를 입력받고, 261행에서 변환할 진수(2~36까지의 정수)를 입력받는다.
#그 뒤 265행에서는 card_conv()함수를 호출하여 반환된 문자열을 출력한다.

#실습 2-7[A]의 card_conv()함수 부분을 다음과 같이 수정하여 기수 변환하는 과정을 자세히 나타냈다.

#10진수 정숫값을 입력받아 2~36진수로 변환하여 출력하기(실습2-7[A]수정)

def card_conv(x:int, r:int) -> str :
    '''정숫값 x를 r진수로 변환한 뒤 그 수를 나타내는 문자열을 반환'''

    d = ''  #변환 후의 문자열
    dchar = '0123456789ABCDEFGHIJKLNMOPQRSTUVWXYZ'
    n = len(str(x)) #변환하기 전의 자릿수

    print(f'{r:2} | {x:{n}d}')
    while x > 0 :
        print(' +' + (n + 2) * '-')
        if x // r:
            print(f'{r:2} | {x // r:{n}d} --- {x%r}')
        else :
            print(f'     {x // r:{n}d} --- {x%r}')
        d += dchar [x%r] #해당하는 문자열을 꺼내 결합
        x //= r

    return d[::-1] #역순으로 변환

if __name__ == '__main__' :
    print('10진수를 n진수로 변환한다.')

    while True :
        while True : #음이 아닌 정수를 입력받음.
            no = int(input('변환할 값으로 음이 아닌 정수를 입력하세요. :'))
            if no > 0:
                break

        while True : #2~36진수의 정숫값을 입력받는다.
            cd = int(input('어떤 진수로 변환할까요? :'))
            if 2 <= cd <= 36 :
                break

        print(f'{cd}진수로는 {card_conv(no,cd)}입니다.')

        retry = input('한 번 더 변환할까요? (Y -- 예 / N -- 아니요) :')
        if retry in {'N', 'n'} :
             break

#함수 사이에 인수 주고받기
#실습 2C-5

def sum_1ton(n) :
    """1부터 n까지 정수의 합"""
    s = 0
    while n > 0 :
        s += n
        n -= 1
    return s

x = int(input('x의 값을 입력하세요. :'))
print(f'1부터 {x}까지 정수의 합은 {sum_1ton(x)}입니다.')

#파이썬에서는 매개변수에 실제 인수가 대입된다.
#함수의 실행 시작 시점에서 매개변수는 실제 인수와 같은 객체를 참조한다. 함수에서 매개변수의 값을 변경하면 인수의 형(type)에 따라 다음과 같이 구분된다.
#1. 인수가 이뮤터블일때 : 함수 안에서 매개변수의 값을 변경하면 다른 객체를 생성하고, 그 객체에 대한 참조로 업데이트한다. 따라서 매개변수의 값을 변경해도 호출하는 쪽의 실제 인수에는 영향을 주지 않는다.
#2. 인수가 뮤터블일때 : 함수 안에서 매개변수의 값을 변경하면 객체 자체를 업데이트한다. 따라서 매개변수의 값을 변경하면 호출되는 쪽의 실제 인수는 값이 변경된다.


#실습 2C-6
#리스트에서 임의의 원솟값을 업데이트하기

def change(lst, idx, val) :
    """lst[idx]의 값을 val로 업데이트"""
    lst[idx] = val

x = [11, 22, 33, 44, 55]
print('x=', x)

index = int(input('업데이트할 인덱스를 선택하시오.: '))
value = int(input('새로운 값을 입력하세요. :'))

change(x, index, value)
print(f'x = {x}')