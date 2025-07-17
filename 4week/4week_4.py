'''
https://school.programmers.co.kr/learn/courses/30/lessons/142086
가장 가까운 글자

문제 설명
문자열 s가 주어졌을 때, s의 각 위치마다 자신보다 앞에 나왔으면서,
자신과 가장 가까운 곳에 있는 같은 글자가 어디 있는지 알고 싶습니다.
예를 들어, s="banana"라고 할 때,
각 글자들을 왼쪽부터 오른쪽으로 읽어 나가면서 다음과 같이 진행할 수 있습니다.

b는 처음 나왔기 때문에 자신의 앞에 같은 글자가 없습니다. 이는 -1로 표현합니다.
a는 처음 나왔기 때문에 자신의 앞에 같은 글자가 없습니다. 이는 -1로 표현합니다.
n은 처음 나왔기 때문에 자신의 앞에 같은 글자가 없습니다. 이는 -1로 표현합니다.
a는 자신보다 두 칸 앞에 a가 있습니다. 이는 2로 표현합니다.
n도 자신보다 두 칸 앞에 n이 있습니다. 이는 2로 표현합니다.
a는 자신보다 두 칸, 네 칸 앞에 a가 있습니다. 이 중 가까운 것은 두 칸 앞이고, 이는 2로 표현합니다.
따라서 최종 결과물은 [-1, -1, -1, 2, 2, 2]가 됩니다.

문자열 s이 주어질 때, 위와 같이 정의된 연산을 수행하는 함수 solution을 완성해주세요.


제한사항
1 ≤ s의 길이 ≤ 10,000
s은 영어 소문자로만 이루어져 있습니다.

s	        result
"banana"	[-1, -1, -1, 2, 2, 2]
"foobar"	[-1, -1, 1, -1, -1, -1]
'''

def solution(s):
    answer = []

    j = []
    for a in range(len(s)):
        j.append(s[a])
    answer.append(-1)

    k = []
    for a in range(len(s)):
        k.append(s[a])
    k.reverse()

    n = len(j) + 1 #n은 k배열에서 시작할 순서

    for i in j[1:]:
        sum = 1 #sum은 안쪽 for문을 돌리는 횟수,
        n -= 1 #n은 for문을 돌릴때마다 1씩 빼줌, 이유는 j배열이 하나씩 넘어갈때 k배열도 하나씩 늘려야함.
        for t in k[n -1:]:
            c = len(k[n -1 :]) #c는 안쪽 for문이 돌리다 t값이 i값이랑 같아지는 경우에 멈추고 -1을 반환하기 위해 넣어둔 변수
            if i != t and sum != c: #i와 t가 다르고, sum이 c와 다를때 즉, sum+=1 한번돌렸다는걸 알려줌
                sum += 1
            elif i != t and sum == c: #i와 t가 다르고, sum이랑 c가 같다 즉, i의 값과 k배열을 계속 돌려서 i값 전까지왔는데 같은게 없다? -1 변환한다.
                answer.append(-1)
                break
            elif i == t: #i와 t가 같으면 돌린횟수(즉, i의 뒤에서 몇번째에 값이있는지)를 answer에 넣음.
                answer.append(sum)
                break

    return answer

print(solution("banana"))
print(solution("foobar"))


