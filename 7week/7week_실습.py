#실습 2-8
#1000이하의 소수를 나열하기

counter = 0 #나눗셈 횟수를 카운트

for n in range(2, 1001) :
    for i in range(2,n) :
        counter += 1
        if n % i == 0 : # 나누어 떨어지면 소수가 아님
            break
    else :
        print(n)
print(f'나눗셈을 실행한 횟수: {counter}')

#실습 2-9
#1000이하의 소수를 나열하기(알고리즘 개선1)

counter = 0 # 나눗셈 횟수를 카운트
ptr = 0 # 이미 찾은 소수의 개수
prime = [None] * 500 # 소수를 저장하는 배열

prime[ptr] = 2 #2는 소수이므로 초깃값으로 지정
ptr += 1

for n in range(3, 1001 , 2) : #홀수만을 대상으로 설정
    for i in range(1, ptr) : #이미 찾은 소수로 나눔
        counter += 1
        if n % prime[i] == 0 : #나누어 떨어지면 소수가 아님
            break # 반복 중단
    else : # 끝까지 나누어 떨어지지 않는다면
        prime[ptr] = n #소수로 배열에 등록
        ptr += 1

for i in range(ptr) : #ptr의 소수를 출력
    print(prime[i])
print(f'나눗셈을 실행한 횟수 : {counter}')


#실습 2-10
#1000 이하의 소수를 나열하기(알고리즘 개선 2)

counter = 0
ptr = 0
prime = [None] * 500

prime[ptr] = 2 #2는 소수
ptr += 1

prime[ptr] = 3 #3은 소수
ptr += 1

for n in range(5, 1001, 2) : #홀수만을 대상으로 설정
    i = 1
    while prime[i] * prime[i] <= n :
        counter += 2
        if n % prime[i] == 0 : #나누어 떨어지면 소수가 아님
            break #반복 중단
        i += 1
    else :
        prime[ptr] = n
        ptr += 1
        counter += 1

for i in range(ptr) : #ptr의 소수를 출력
    print(prime[i])
print(f'곱셈과 나눗셈을 실행한 횟수 : {counter}')

#실습 2-7
#자료형을 정하지 않은 리스트 원소 확인하기

x = [15, 64, 7, 3.14, [32,55], 'ABC']
for i in range(len(x)) :
    print(f'x[{i}] = {x[i]}')

