import sys


def color_check(graph, size, x, y):
    global blue, white
    sd = graph[x][y]
    flag = True
    for i in range(x, x + size):
        for j in range(y, y + size):
            if graph[i][j] != sd:
                flag = False
                color_check(graph, size // 2, x + size//2, y)
                color_check(graph, size // 2, x + size//2, y + size // 2)
                color_check(graph, size // 2, x, y + size // 2)
                color_check(graph, size // 2, x, y)
                return 0
    if flag:
        if sd == 1:
            blue += 1
        else:
            white += 1
        return 0


if __name__ == "__main__":
    n = int(input())

    white, blue = 0, 0

    # 색종이 정보 입력받기
    graph = []
    for _ in range(n):
        graph.append(list(map(int, sys.stdin.readline().split())))

    color_check(graph, n, 0, 0)
    print(white)
    print(blue)
