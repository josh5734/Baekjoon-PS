

if __name__ == "__main__":
    bucket = list(input())
    answer = 0

    # 괄호들을 담을 스택을 생성
    stack = []

    # 첫문째 괄호를 스택에 삽입
    stack.append(bucket[0])

    inside = 0
    for b in bucket[1:]:
        # 스택에 아직 괄호가 남아있는 동안에는 그 안의 값을 계산
        if len(stack) != 0:
            print(stack)
            # 여는 괄호이면 삽입
            if b == '(' or b == '[':
                stack.append(b)
            # 닫는 소괄호이고 스택의 끝 값이 여는 소괄호이면 스택에서 pop
            elif b == ')' and stack[-1] == '(':
                stack.pop()
                # 아직 열린 괄호인 상태면 곱하기
                if len(stack) != 0:
                    if stack[-1] == '(' or stack[-1] == '[':
                        inside += 2
                else:
                    inside *= 2
                    answer += inside
            # 닫는 대괄호이고 스택의 끝 값이 닫는  대괄호이면 스택에서 pop
            elif b == ']' and stack[-1] == '[':
                temp = stack.pop()
                if len(stack) != 0:
                    if stack[-1] == '(' or stack[-1] == '[':
                        inside += 3
                else:
                    inside *= 3
                    answer += inside

    print(answer)
