"""
https://school.programmers.co.kr/learn/courses/30/lessons/42583
"""
from collections import deque

def summ(a) :   #합
    sum_1 = 0
    for i in a :
        sum_1 += i[0]
    return sum_1

def solution(bridge_length, weight, truck_weights):
    answer = 0
    truck_weights = deque(truck_weights)
    bridge_truck = deque()
    while len(bridge_truck) != 0 or len(truck_weights) != 0:
        answer += 1
        if len(bridge_truck) >0 and bridge_truck[0][1] + bridge_length <= answer:
            bridge_truck.popleft()

        if len(truck_weights) > 0:
            bridge_sum = summ(bridge_truck)

            if bridge_sum + truck_weights[0] <= weight and len(bridge_truck) < bridge_length:
                bridge_truck.append((truck_weights.popleft(), answer))

    return answer

print(solution(2,10,[7,4,5,6]))
print(solution(100,100,[10]))
print(solution(100,100,[10,10,10,10,10,10,10,10,10,10]))