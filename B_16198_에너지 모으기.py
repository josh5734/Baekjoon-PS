import copy

def backTracking(marble, x, energy):
    global answer
    energy += marble[x-1] * marble[x+1]
    marble.pop(x)

    # 구슬의 개수가 2개 남으면 선택 종료
    if len(marble) == 2:
        if energy > answer:
            answer = energy
        return

    for i in range(1, len(marble)-1):
        temp = copy.deepcopy(marble)
        backTracking(temp, i, energy)

n = int(input())
weight = list(map(int, input().split()))
answer = 0

# 구슬을 선택하는 모든 경우의 수를 다 해본다.
for i in range(1, len(weight)-1):
    temp = copy.deepcopy(weight)
    backTracking(temp, i, 0)

print(answer)