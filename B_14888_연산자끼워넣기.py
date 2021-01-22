from itertools import permutations as p


def calculate(op):
    # 연산자의 개수만큼 연산 시행
    for i in range(n-1):
        # 첫번째 값 설정
        if i == 0:
            if op[i] == '+':
                start = sequence[i] + sequence[i+1]
            elif op[i] == '-':
                start = sequence[i] - sequence[i+1]
            elif op[i] == '*':
                start = sequence[i] * sequence[i+1]
            else:
                start = sequence[i] // sequence[i+1]
        else:
            if op[i] == '+':
                start += sequence[i+1]
            elif op[i] == '-':
                start -= sequence[i+1]
            elif op[i] == '*':
                start *= sequence[i+1]
            else:
                if start < 0:
                    start = ((start * -1) // sequence[i+1]) * -1
                else:
                    start //= sequence[i+1]
    answer.append(start)


if __name__ == "__main__":
    n = int(input())
    sequence = list(map(int, input().split()))
    type = ['+', '-', '*', '%']
    ops = ""
    # 각 연산자의 수만큼 String 형태로 쌓는다.
    line = list(map(int, input().split()))
    for t, c in zip(type, line):
        ops += t * c

    answer = []
    # 모든 경우의 수에 대해 진행 / 중복 제외
    comb = set(list(p(ops)))
    for op in comb:
        calculate(op)

    # 최대, 최소 출력
    print(max(answer))
    print(min(answer))
