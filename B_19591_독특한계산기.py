import sys
from collections import deque


def solve(numbers, calc):
    while True:
        if len(numbers) == 1:
            return numbers[0]
        if calc[0] in ['*', '/'] and calc[-1] in ['+', '-']:
            a, b = numbers.popleft(), numbers.popleft()
            if calc[0] == '*':
                numbers.appendleft(a*b)
            else:
                numbers.appendleft(int(a/b))
            calc.popleft()
        elif calc[0] in ['+', '-'] and calc[-1] in ['*', '/']:
            b, a = numbers.pop(), numbers.pop()
            if calc[-1] == '*':
                numbers.append(a*b)
            else:
                numbers.append(int(a/b))
            calc.pop()
        else:
            a, b = 0, 0
            if calc[0] in ['+', '-']:
                a = numbers[0] + \
                    numbers[1] if calc[0] == '+' else numbers[0] - numbers[1]
                b = numbers[-1] + \
                    numbers[-2] if calc[-1] == '+' else numbers[-2] - \
                    numbers[-1]

            else:
                a = numbers[0] * \
                    numbers[1] if calc[0] == '*' else int(
                        numbers[0] / numbers[1])
                b = numbers[-2] * \
                    numbers[-1] if calc[-1] == '*' else int(
                        numbers[-2] / numbers[-1])

            if a >= b:
                numbers.popleft()
                numbers.popleft()
                numbers.appendleft(a)
                calc.popleft()
            else:
                numbers.pop()
                numbers.pop()
                numbers.append(b)
                calc.pop()


if __name__ == "__main__":

    # 숫자와 연산자를 순서대로 담는 리스트
    numbers = deque()
    calc = deque()
    info = sys.stdin.readline().rstrip()
    # 숫자, 연산자 정보 입력 -> -처리, 불필요한 0처리
    temp = ""
    for i in range(len(info)):
        if info[i].isdigit():
            temp += info[i]
            if i == len(info)-1:
                numbers.append(int(temp))
                temp = ""
        else:
            if temp != "":
                numbers.append(int(temp))
                calc.append(info[i])
                temp = ""
    if len(info) != 0:
        if info[0] == '-':
            numbers[0] *= -1
        answer = solve(numbers, calc)
        print(answer)
    else:
        print()
