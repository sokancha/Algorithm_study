#실습 1-1
#세 정수를 입력받아  최댓값 구하기

'''print('세 정수의 최댓값을 구합니다.')

a = int(input('정수 a의 값을 입력하세요. :'))
b = int(input('정수 b의 값을 입력하세요. :'))
c = int(input('정수 c의 값을 입력하세요. :'))

maximum = a
if b > maximum: maximum = b
if c > maximum: maximum = c

print(f'최대값은 {maximum}입니다.')

#실습1C-1
#이름을 입력받아 인사하기
print('이름을 입력하세요 :', end = '')
name = input()
print(f'안녕하세요? {name}님.')



#실습1C-2
#이름을 입력받아 인사하기
name = input('이름을 입력하세요. :')
print(f'안녕하세요? {name}님.')



#실습 1-2
#세 정수의 최댓값 구하기

def max3(a,b,c) :
    """a,b,c의 최댓값을 구하여 반환"""
    maximum = a
    if b > maximum : maximum = b
    if c > maximum : maximum = c
    return maximum #최댓값 변환

print(f'max3(3,2,1) = {max3(3,2,1)}')
print(f'max3(3,2,2) = {max3(3,2,2)}')
print(f'max3(3,1,2) = {max3(3,1,2)}')
print(f'max3(3,2,3) = {max3(3,2,3)}')
print(f'max3(2,1,3) = {max3(2,1,3)}')
print(f'max3(3,3,2) = {max3(3,3,2)}')
print(f'max3(3,3,3) = {max3(3,3,3)}')
print(f'max3(2,2,3) = {max3(2,2,3)}')
print(f'max3(2,3,1) = {max3(2,3,1)}')
print(f'max3(2,3,2) = {max3(2,3,2)}')
print(f'max3(1,3,2) = {max3(1,3,2)}')
print(f'max3(2,3,3) = {max3(2,3,3)}')
print(f'max3(1,2,3) = {max3(1,2,3)}')


#실습 1C-2
#세 정수를 입력받아 중앙값 구하기 1

def med3(a,b,c) :
    """a,b,c의 중앙값을 구하여 반환"""
    if a >= b :
        if b >= c :
            return b
        elif a <= c :
            return a
        else :
            return c
    elif a > c :
        return a
    elif b > c :
        return c
    else :
        return b

print('세 정수의 중앙값을 구합니다.')
a = int(input('정수 a의 값을 입력하세요. :'))
b = int(input('정수 b의 값을 입력하세요. :'))
c = int(input('정수 c의 값을 입력하세요. :'))

print(f'중앙값은 {med3(a,b,c)}입니다.')


#실습 1-3
#입력받은 정수의 부호(양수,음수,0)출력하기

n = int(input('정수를 입력하세요. :'))

if n > 0 :
    print('이 수는 양수입니다.')
elif n < 0 :
    print('이 수는 음수입니다.')
else :
    print('이 수는 0입니다.')


#실습 1-4
#3개로 분기하는 조건문

n = int(input('정수를 입력하세요. :'))

if n == 1:
    print('A')
elif n == 2 :
    print('B')
else :
    print('C')


#실습 1-4
#4개로 분기하는 조건문

n = int(input('정수를 입력하세요. :'))

if n ==1 :
    print('A')
elif n ==2 :
    print('B')
elif n == 3 :
    print('C')


#실습 1-6
#실습 1-5의 원래모습

n = int(input('정수를 입력하세요. :'))

if n ==1 :
    print('A')
elif n ==2 :
    print('B')
elif n == 3 :
    print('C')
else :
    pass

'''


