import sys


def floyd():
    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])


if __name__ == "__main__":
    INF = int(1e9)
    # 도시의 개수 n, 버스의 개수 m
    n = int(input())
    m = int(input())

    # 그래프 정보 입력받기
    graph = [[INF] * (n+1) for _ in range(n+1)]

    for i in range(1, n+1):
        for j in range(1, n+1):
            if i == j:
                graph[i][j] = 0

    # sour -> dest : cost 정보 입력받기
    for _ in range(m):
        sour, dest, cost = map(int, sys.stdin.readline().split())
        # 더 적은 비용으로 갈 수 있는 경로로 설정
        if graph[sour][dest] > cost:
            graph[sour][dest] = cost

    # floyd 알고리즘 수행
    floyd()

    # 결과 출력
    for i in range(1, n+1):
        for j in range(1, n+1):
            # 도달할 수 없으면 0을 출력
            if graph[i][j] == INF:
                print("0", end=" ")
            else:
                print(graph[i][j], end=" ")
        print()
