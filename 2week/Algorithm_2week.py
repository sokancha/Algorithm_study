#문제 1
#https://school.programmers.co.kr/learn/courses/30/lessons/340207
"""주어진 코드는 변수에 데이터를 저장하고 출력하는 코드입니다.
아래와 같이 출력되도록 빈칸을 채워 코드를 완성해 주세요."""

message = "Let's go!" #빈칸

print("3 \n 2 \n 1") # \n 빈칸

print(message)

#문제2
#https://school.programmers.co.kr/learn/courses/30/lessons/340206
"""일반적으로 두 선분이 이루는 각도는 한 바퀴를 360도로 하여 표현합니다. 
따라서 각도에 360의 배수를 더하거나 빼더라도 같은 각을 의미합니다. 
예를 들면, 30도와 390도는 같은 각도입니다.

주어진 코드는 각도를 나타내는 두 정수 angle1과 angle2가 주어질 때, 
이 두 각의 합을 0도 이상 360도 미만으로 출력하는 코드입니다. 
코드가 올바르게 작동하도록 한 줄을 수정해 주세요."""

angle1 = int(input())
angle2 = int(input())

sum_angle = (angle1 + angle2) - (360 * int((angle1 + angle2) / 360))
print(sum_angle)

#문제3
#https://school.programmers.co.kr/learn/courses/30/lessons/250133
"""주어진 초기 코드는 변수에 데이터를 저장하고 출력하는 코드입니다. 
아래와 같이 출력되도록 빈칸을 채워 코드를 완성해 주세요."""

string_msg = "Spring is beginning"
int_val = 3
string_val = "3"

print(string_msg)
print(int_val + 10)
print(string_val + "10")


#문제4
#https://school.programmers.co.kr/learn/courses/30/lessons/250132
"""직각삼각형이 주어졌을 때 빗변의 제곱은 다른 두 변을 각각 제곱한 것의 합과 같습니다.

직각삼각형의 한 변의 길이를 나타내는 정수 a와 빗변의 길이를 나타내는 정수 c가 주어질 때, 
다른 한 변의 길이의 제곱, b_square 을 출력하도록 한 줄을 수정해 코드를 완성해 주세요."""

a = int(input())
c = int(input())

b_square = c*c - a*a
print(b_square)

#문제5
#https://school.programmers.co.kr/learn/courses/30/lessons/250130
"""진우는 돈을 모으기 위해 저축을 하려고 합니다. 목표로 하는 금액은 100만 원이며,
 첫 달에 일정 금액을 넣은 뒤 70만 원까지는 매월 조금씩
 저축하다가 70만 원 이후부터는 월 저축량을 늘려 빠르게 목표 금액을 달성하고자 합니다.

첫 달에 저축하는 금액을 나타내는 정수 start, 두 번째 달 부터 70만 원 이상 모일 때까지 
매월 저축하는 금액을 나타내는 정수 before, 100만 원 이상 모일 때 까지 매월 저축하는 금액을 
나타내는 정수 after가 주어질 때, 100만 원 이상을 모을 때까지 
걸리는 개월 수를 출력하도록 빈칸을 채워 코드를 완성해 주세요."""

start = int(input())
before = int(input())
after = int(input())

money = start
month = 1
while money < 70:
    money += before
    month += 1
while money < 100 :
    money += after
    month += 1

print(month)



#같이 풀어볼 문제
#https://school.programmers.co.kr/learn/courses/30/lessons/340205
"""2자리 이상의 정수 number가 주어집니다. 주어진 코드는 이 수를 2자리씩 자른 뒤, 
자른 수를 모두 더해서 그 합을 출력하는 코드입니다. 
코드가 올바르게 작동하도록 한 줄을 수정해 주세요."""

number = int(input())

answer = 0

for i in range(1):
    answer += number % 100
    answer += (number // 100)

print(answer)