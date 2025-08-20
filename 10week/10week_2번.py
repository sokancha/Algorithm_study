def solution(keymap, targets):
    answer = []
    for i in targets :
        sum = 0 # targets단어를 총 몇 번 눌러야하는지 합해줄 변수
        for j in i :
            index = 0 # keymap에서 인덱스를 지정할 변수
            sum_index = 0 # target의 j별로 몇 번 눌러야하는지 더해줄 인덱스
            while True :
                for k in keymap : #keymap의 첫단어부터 하나씩 j와 같은게 있는지 찾기
                    if k[index] == j : #index가 0부터 시작해서 첫단어부터 같은게 있는지 확인
                        sum_index += index + 1 # 있으면 sum_index에 저장
                        break #for문종료
                index += 1 #for문이 실행되지않았을 때 즉, index번째에 맞는 단어가 없을때 다음단어로 이동
                if sum_index != 0 : #단어가 있을때 sum_index값이 0이아닐때, while문 종료
                    break
                if index == len(k) : #단어가 없어서 for문이 다돌아갔지만 없을때, -1로 반환
                    sum_index = -1
                    break
            if sum_index == -1 : #while문이 끝났을때 최종적으로 sum_index가 -1이면 -1반환
                sum = sum_index
                break
            sum += sum_index #그게 아니라면 sum에 sum_index 계속 더해주고
        answer.append(sum) #최종적으로 단어 i에 대한 for문이 끝났을때 결과에 넣어줌
    return answer

print(solution(["ABACD", "BCEFD"],["ABCD","AABB"]))
print(solution(["AA"],["B"]))
print(solution(["AGZ", "BSSS"],["ASA","BGZ"]))