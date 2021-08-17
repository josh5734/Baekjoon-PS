import sys


def canContainRain(x, y):  # 해당 블록 기준 좌우에 벽이 모두 있는지 확인
    leftWall, rightWall = False, False
    for b in graph[x][:y]:
        if b == 1:
            leftWall = True
            break
    for b in graph[x][y+1:]:
        if b == 1:
            rightWall = True
            break

    return leftWall and rightWall


if __name__ == "__main__":
    h, w = map(int, input().split())
    graph = [[0] * w for _ in range(h)]
    rain = list(map(int, input().split()))

    # 현재 블록 채우기
    curr = 0
    for r in rain:
        for i in range(h-r, h):
            graph[i][curr] = 1
        curr += 1

    answer = 0
    for i in range(h-1, -1, -1):
        for j in range(w):
            # 양끝에 있지 않고 현재 빈 블록에 대해서
            if j != 0 and j != w-1 and graph[i][j] == 0:
                if canContainRain(i, j) == True:  # 빗물을 채울 수 있는지 확인
                    graph[i][j] = 1
                    answer += 1
    print(answer)


################## 풀이 2 ##########################

if __name__ == "__main__":
    h, w = map(int, input().split())
    rain = list(map(int, input().split()))

    answer = 0
    for i in range(1, w-1):  # 양쪽 끝 제외
        leftMax, rightMax = max(rain[:i]), max(rain[i+1:])
        if min(leftMax, rightMax) >= rain[i]:
            answer += min(leftMax, rightMax) - rain[i]
    print(answer)
