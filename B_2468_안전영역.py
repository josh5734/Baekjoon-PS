import copy
from sys import setrecursionlimit

# 재귀 깊이를 설정해줌으로써 runtimeError를 방지해야함
setrecursionlimit(10 ** 6)


def count_safe_region(graph, x, y, rain):

    # 범위를 벗어나면 종료
    if x <= -1 or x >= n or y <= -1 or y >= n:
        return False

    # 침수되지 않은 인접한 도시가 있다면 방문
    if graph[x][y] > rain:
        # 해당 도시를 방문 체크
        graph[x][y] = -1
        # 상,하,좌,우 재귀 호출
        count_safe_region(graph, x-1, y, rain)
        count_safe_region(graph, x, y-1, rain)
        count_safe_region(graph, x+1, y, rain)
        count_safe_region(graph, x, y+1, rain)
        return True
    return False


if __name__ == "__main__":

    # 그래프 정보 입력받기
    n = int(input())
    graph = []
    for i in range(n):
        graph.append(list(map(int, input().split())))

    # 비의 높이마다 안전 영역의 수를 저장할 리스트
    safe_region = [0] * 101
    rain = 0
    # 실행은 높이가 0부터 최대 100까지 반복 수행
    while(rain <= 100):
        # rain의 높이가 달라질때마다 같은 그래프를 사용할 수 있도록 deepcopy.
        temp = copy.deepcopy(graph)
        for x in range(n):
            for y in range(n):
                # 높이가 i, 현재 위치가 x,y일때 dfs 수행
                if count_safe_region(temp, x, y, rain) == True:
                    safe_region[rain] += 1
        rain += 1
    print(max(safe_region))
