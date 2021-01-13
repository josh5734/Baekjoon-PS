import sys


def tetro1(x, y):  # ㅡ
    if y + 3 < m:
        tetromino_sum.append(sum(graph[x][y:y+4]))
    if x + 3 < n:
        col_sum = 0
        for i in range(x, x+4):
            col_sum += graph[i][y]
        tetromino_sum.append(col_sum)


def tetro2(x, y):  # ㅁ
    if x+1 < n and y+1 < m:
        tetromino_sum.append(graph[x][y]+graph[x+1]
                             [y]+graph[x][y+1]+graph[x+1][y+1])


def tetro3(x, y):  # ㄱ
    if x+2 < n and y+1 < m:
        tetromino_sum.append(graph[x][y]+graph[x+1]
                             [y]+graph[x+2][y]+graph[x+2][y+1])

    if x+2 < n and y-1 >= 0:
        tetromino_sum.append(graph[x][y]+graph[x+1]
                             [y]+graph[x+2][y]+graph[x+2][y-1])

    if x+1 < n and y+2 < m:
        tetromino_sum.append(graph[x][y]+graph[x+1]
                             [y]+graph[x+1][y+1]+graph[x+1][y+2])

    if x+1 < n and y-2 >= 0:
        tetromino_sum.append(graph[x][y]+graph[x+1]
                             [y]+graph[x][y-1]+graph[x][y-2])

    if x+1 < n and y+2 < m:
        tetromino_sum.append(graph[x][y]+graph[x+1]
                             [y]+graph[x][y+1]+graph[x][y+2])

    if x+1 < n and y-2 >= 0:
        tetromino_sum.append(graph[x][y]+graph[x+1]
                             [y]+graph[x+1][y-1]+graph[x+1][y-2])

    if x-2 >= 0 and y+1 < m:
        tetromino_sum.append(graph[x][y]+graph[x-1]
                             [y]+graph[x-2][y]+graph[x-2][y+1])

    if x-2 >= 0 and y-1 >= 0:
        tetromino_sum.append(graph[x][y]+graph[x-1]
                             [y]+graph[x-2][y]+graph[x-2][y-1])


def tetro4(x, y):  # ㄹ
    if x+2 < n and y+1 < m:
        tetromino_sum.append(graph[x][y]+graph[x+1]
                             [y]+graph[x+1][y+1]+graph[x+2][y+1])
    if x-1 >= 0 and y+2 < m:
        tetromino_sum.append(graph[x][y]+graph[x]
                             [y+1]+graph[x-1][y+1]+graph[x-1][y+2])
    if x+2 < n and y-1 >= 0:
        tetromino_sum.append(graph[x][y]+graph[x+1]
                             [y]+graph[x+1][y-1]+graph[x+2][y-1])
    if x+1 < n and y+2 < m:
        tetromino_sum.append(graph[x][y]+graph[x]
                             [y+1]+graph[x+1][y+1]+graph[x+1][y+2])


def tetro5(x, y):  # ㅗ
    if x+1 < n and y-1 >= 0 and y+1 < m:
        tetromino_sum.append(graph[x][y]+graph[x]
                             [y+1]+graph[x][y-1]+graph[x+1][y])
    if x-1 >= 0 and y-1 >= 0 and y+1 < m:
        tetromino_sum.append(graph[x][y]+graph[x-1]
                             [y]+graph[x][y-1]+graph[x][y+1])
    if x-1 >= 0 and x+1 < n and y+1 < m:
        tetromino_sum.append(graph[x][y]+graph[x-1]
                             [y]+graph[x+1][y]+graph[x][y+1])
    if x-1 >= 0 and x+1 < n and y-1 >= 0:
        tetromino_sum.append(graph[x][y]+graph[x-1]
                             [y]+graph[x+1][y]+graph[x][y-1])


if __name__ == "__main__":

    # n, m 입력받기
    n, m = map(int, input().split())

    # 그래프 정보
    graph = []
    for _ in range(n):
        graph.append(list(map(int, sys.stdin.readline().split())))

    # 가능한 모든 테트로미노의 합
    tetromino_sum = []
    for i in range(n):
        for j in range(m):
            tetro1(i, j)
            tetro2(i, j)
            tetro3(i, j)
            tetro4(i, j)
            tetro5(i, j)
    print(max(tetromino_sum))
