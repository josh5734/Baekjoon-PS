import sys, heapq


def dijkstra(graph, cost, x, y):
    n = len(graph)
    pq = []

    # 초기 비용을 우선순위 큐에 넣고 시작
    heapq.heappush(pq, (graph[x][y], x,y))
    while pq:
        curr_cost, curr_x, curr_y = heapq.heappop(pq)
        # 이미 최소 비용을 구했으면 무시한다.
        if cost[curr_x][curr_y] < curr_cost:
            continue

        for i in range(4):
            next_x, next_y = curr_x + dx[i], curr_y + dy[i]
            if 0 <= next_x < n and 0 <= next_y < n:
                next_cost = graph[next_x][next_y] 
                if curr_cost + next_cost < cost[next_x][next_y]:
                    heapq.heappush(pq, (curr_cost + next_cost, next_x, next_y))
                    cost[next_x][next_y] = curr_cost + next_cost
        
    return cost[n-1][n-1]


input = sys.stdin.readline
dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
inf = int(1e5)
tc = 1
while True:
    n = int(input())
    if n == 0: break # 0을 입력받으면 종료

    graph = [list(map(int, input().split())) for _ in range(n)]
    # 시작점(0,0)부터 도착지점까지 잃게 되는 루피의 크기
    cost = [[inf] * n for _ in range(n)]

    # 결과 출력하기
    answer = dijkstra(graph, cost, 0, 0)
    print('Problem {}: {}'.format(tc, answer))
    tc += 1