import sys

if __name__ == "__main__":
    # n,m 입력받기
    n, m = map(int, input().split())

    # graph 입력받기
    graph = [[] for _ in range(n)]
    partial_sum = [[0]*n for _ in range(n)]
    for i in range(n):
        graph[i] = list(map(int, sys.stdin.readline().split()))
        line_sum = 0
        # 각 위치마다 원점(1,1)을 기준으로 그곳까지의 직사각형 합을 구함
        for j in range(n):
            line_sum += graph[i][j]
            if i == 0:
                partial_sum[i][j] = line_sum
            else:
                partial_sum[i][j] = partial_sum[i-1][j] + line_sum

    # (x1,y1 ~ x2,y2까지의 합) = 아래의 4가지 규칙에 따라 격자 모양을 다르게 계산
    for _ in range(m):
        x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
        total = 0
        if x1 == 1 and y1 != 1:
            total = partial_sum[x2-1][y2-1] - partial_sum[x2-1][y1-2]

        elif y1 == 1 and x1 != 1:
            total = partial_sum[x2-1][y2-1] - partial_sum[x1-2][y2 - 1]

        elif x1 == 1 and y1 == 1:
            total = partial_sum[x2-1][y2-1]
        else:
            total = partial_sum[x2-1][y2-1] - partial_sum[x1-2][y2 -
                                                                1] - partial_sum[x2-1][y1-2] + partial_sum[x1-2][y1-2]
        print(total)
