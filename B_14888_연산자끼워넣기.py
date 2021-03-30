from itertools import permutations as p


def calculate(op):
    # 연산자의 개수만큼 연산 시행
    start = sequence[0]
    for i in range(n-1):
        if op[i] == '+':
            start += sequence[i+1]
        elif op[i] == '-':
            start -= sequence[i+1]
        elif op[i] == '*':
            start *= sequence[i+1]
        else:  # 앞에서부터 계산하므로 0으로 나누는 경우는 없음
            start = int(start/sequence[i+1])
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
    minV, maxV = int(1e10), -int(1e10)
    for op in comb:
        calculate(op)

    # 최대, 최소 출력
    print(max(answer))
    print(min(answer))


############## 풀이2 - DFS 쓰기 ################


def calculateByDFS(root, count, plus, minus, multiply, divide):
    if count == n-1:
        result.append(root)

    if plus > 0:
        calculateByDFS(root+sequence[count+1],
                       count+1, plus-1, minus, multiply, divide)
    if minus > 0:
        calculateByDFS(root-sequence[count+1],
                       count+1, plus, minus-1, multiply, divide)
    if multiply > 0:
        calculateByDFS(root*sequence[count+1],
                       count+1, plus, minus, multiply-1, divide)
    if divide > 0:
        calculateByDFS(int(root/sequence[count+1]),
                       count+1, plus, minus, multiply, divide-1)


result = []
if __name__ == "__main__":
    n = int(input())
    sequence = list(map(int, input().split()))
    plus, minus, multiply, divide = map(int, input().split())
    minValue, maxValue = int(1e10), -int(1e10)
    calculateByDFS(sequence[0], 0, plus, minus, multiply, divide)
    print(max(result))
    print(min(result))
