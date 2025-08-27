'''
https://school.programmers.co.kr/learn/courses/30/lessons/12906
'''
class FixedStack:
    class Empty(Exception):
        pass

    # 비어 있는 FixedStack에 피크할 때 내보내는 예외 처리

    def __init__(self):
        self.stk = []

    # 스택 초기화

    def is_empty(self) -> bool:
        return not self.stk

    # 스택이 비어 있는지 확인

    def push(self, item):
        self.stk.append(item)

    # 스택에 item을 푸시

    def peek(self):
        if self.is_empty():
            raise FixedStack.Empty
        return self.stk[-1]

    # 스택에서 데이터를 피크(is_empty가 True이면 즉, 데이터가 비어 있다면 Empty예외처리를 보냄)

    def dump(self) -> None:
        if self.is_empty():
            print('스택이 비어 있음')
            # 위랑 똑같이 비어있으면 비어있음을 출력
        else:
            return self.stk
            # 그게 아니면 스택전체를 반환


def solution(arr):
    answer = []

    s = FixedStack()
    # FixedStack클래스의 인스턴스 생성

    s.push(arr[0])
    # arr의 0번째 원소를 푸시(어차피 첫번째는 겹치던 안겹치던 상관없으니까)

    for i in arr[1:]:
        if i != s.peek():
            s.push(i)
    # 반복문으로 arr의 두번째원소부터 끝원소까지 반복
    # i가 스택의 맨 위(꼭대기)와 비교하여 다를 경우 -> 연속되지 않은 숫자 -> 스택에 i를 푸시

    return s.dump()
    # 최종적으로 스택이 완료되면 스택전체를 반환한다.

print(solution([1,1,3,3,0,1,1]))
print(solution([4,4,4,3,3]))