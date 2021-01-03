

if __name__ == "__main__":
    str = list(input())
    postfix = ""
    # postfix로 고치기 위한 stack
    stack = []

    high_priority = ['*', '/']
    low_priority = ['+', '-']

    for w in str:

        if w.isalpha():
            postfix += w

        else:
            if w == ')':
                while stack:
                    temp = stack.pop()
                    if temp != '(':
                        postfix += temp
                    else:
                        break
            elif w == '(':
                stack.append(w)

            elif w in high_priority:
                while stack:
                    if stack[-1] in high_priority:
                        postfix += stack.pop()
                    else:
                        break
                stack.append(w)
            elif w in low_priority:
                while stack and stack[-1] != '(':
                    postfix += stack.pop()
                stack.append(w)
    while stack:
        postfix += stack.pop()
    print(postfix)
