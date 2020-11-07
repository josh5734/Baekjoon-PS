

def dfs(graph, x, y, result, info):

    if(x <= -1 or x >= m or y <= -1 or y >= n):
        return False

    # 방문할 수 있다면
    if graph[x][y] == 1:
        # 방문하고 0으로 만들어주고, info에다가 공간을 1씩 더해준다.
        graph[x][y] = 0
        info[result] += 1

        dfs(graph, x-1, y, result, info)
        dfs(graph, x, y-1, result, info)
        dfs(graph, x+1, y, result, info)
        dfs(graph, x, y+1, result, info)
        return True

    return False


if __name__ == "__main__":
    n, m, k = map(int, input().split())
    graph = [[1 for i in range(n)] for j in range(m)]

    # 분리된 공간과 각 공간이 몇칸인지 저장할 변수 생성
    result, cnt = (0, 0)
    info = [0 for i in range(n*m)]

    # 직사각형으로 가려진 부분을 0으로 채우기
    for i in range(k):
        x1, y1, x2, y2 = map(int, input().split())
        for p in range(x1, x2):
            for q in range(y1, y2):
                graph[p][q] = 0

    print(graph)
    # dfs 수행
    for i in range(n):
        for j in range(m):
            if dfs(graph, i, j, result, info) == True:
                result += 1
    # 결과 출력
    print(result)
    for x in sorted(info):
        if x != 0:
            print(x, end=" ")
