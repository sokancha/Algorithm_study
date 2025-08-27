class FixedStack:
    class Empty(Exception):
        pass

    def __init__(self):
        self.stk = []
        self.ptr = 0

    def is_empty(self) -> bool:
        return not self.stk

    def push(self, item):
        self.stk.append(item)

    def peek(self):
        if self.is_empty():
            raise FixedStack.Empty
        return self.stk[-1]


def solution(s):
    answer = True
    sk = FixedStack()
    s_list = []
    for i in range(len(s)):
        s_list.append(s[i])
    a = len(s_list)

    if s[0] == ')':
        answer = False

    else:
        sk.push(s[0])
        del s_list[0]

        num = 0
        while True:
            for i in range(len(s_list)):
                if s_list[i] != sk.peek():
                    sk.push(s_list[i])
                    num += 1
                    del s_list[i]
                    break
            if num + 1 == a:
                answer = True
                break

            if len(s_list) == 1:
                if not '(' in s_list:
                    answer = False
                    break
                if not ')' in s_list:
                    answer = False
                    break

    return answer


print(solution("()()"))
print(solution("(())()"))
print(solution(")()("))
print(solution("(()("))



