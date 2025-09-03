from collections import deque

def summ(a) :   #합
    sum_1 = 0
    for i in a :
        sum_1 += i
    return sum_1

def solution(bridge_length, weight, truck_weights):
    answer = 0
    truck_weights = deque(truck_weights)
    bridge_truck = deque()
    pass_truck = deque()
    while True :
        for i in range(len(truck_weights)) :
            print(f'{truck_weights[i]}시작')
            if summ(bridge_truck) + truck_weights[i] <= weight :    #다리에 오를 트럭과 올라와있는 트럭의 합
                bridge_truck.append(truck_weights[i])   #다리에 탑승
                truck_weights.popleft()
                answer += 1
                print(f'bridge_truck은 {bridge_truck}')
                print(f'truck_weights은 {truck_weights}')
                print(answer)
                break
            elif summ(bridge_truck) + truck_weights[i] > weight :
                if len(bridge_truck) == 1 :
                    answer += bridge_length
                    bridge_truck.append(truck_weights[i])  # 다리에 탑승
                    truck_weights.popleft()
                elif len(bridge_truck) > 1 :
                    answer += 1
                bridge_truck.popleft()
                print(f'bridge_truck은 {bridge_truck}')
                print(f'truck_weights은 {truck_weights}')
                print(answer)
                break
        if len(truck_weights) == 0 :
            answer += bridge_length -1
            print(f'bridge_truck은 {bridge_truck}')
            print(f'truck_weights은 {truck_weights}')
            print(answer)
            break

    return answer

print(solution(2,10,[7,4,5,6]))