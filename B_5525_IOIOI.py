import sys

n = int(input())
length = int(input())
text = sys.stdin.readline().rstrip();

# text 문자열을 IOI 순서대로만 남도록 만들기

stack = []
count = 0
# 처음에 I, 그 다음은 O ... 반복
for i in range(len(text)):
    string = text[i];
    if len(stack) == 0:
        if string == "I":
            stack.append("I")
    else:
        if stack[-1] == "O" and string == "I":
            stack.append("I")
        elif stack[-1] == "I" and string == "O":
            stack.append("O")

        # II가 만들어지면 I 하나로 남김
        elif stack[-1] == string and string == "I":
            stack = ["I"]
        # OO 꼴이 되면 필요 없으니까 빈 스택으로 만들기
        elif stack[-1] == string and string == "O":
            stack = []

    # Pn 꼴이 나온 경우에는 위에 2개를 빼준다.
    # Pn 꼴이 이어서 나올 수 있기 때문에        
    if len(stack) == (2 * n) + 1:
        stack.pop()
        stack.pop()
        count += 1

print(count)