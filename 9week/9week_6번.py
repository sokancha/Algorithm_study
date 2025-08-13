def solution(n, q, ans):
    from itertools import combinations
    answer = 0

    k = 0  # 제일 큰 수 찾기
    for i in range(len(ans)):
        if ans[k] < ans[i]:
            k = i
    print(k)

    com = list(combinations(q[k], ans[k]))  # combinations는 해당 배열에서 경우의수 조합

    q.pop(k)  # q와 ans에서 해당 인덱스 지우고
    ans.pop(k)

    for i in com:
        score = 0  # 배열이 정상적인지(com에 경우의수와 맞아떨어질때)
        for j in range(len(q)):  # q배열 반복
            sum = 0  # q배열의 각 배열마다 겹치는 원소가 있는지 확인하기 위한 카운팅변수
            for a in q[j]:  # q배열안에 원소배열 반복
                if a in i:  # 배열안에 원소가 example에 있다면
                    sum += 1
            if sum > ans[j]:
                com.remove(i)
                break
            else:
                score += 1
        if score == len(q):  # 모든 원소가 다 맞았을때
            print(i)
            l_1 = []
            l_3 = []
            for b in range(len(q)):
                if len(set(q[b]) & set(i)) == ans[b]:
                    exlist = list(set(q[b]) - set(i))
                    l_1 += exlist
            for c in range(len(q)):
                l_2 = []
                if len(set(q[b]) & set(i)) < ans[b]:
                    exlist = list(set(q[c]) - set(l_1))
                    l_2 += exlist

    return answer

