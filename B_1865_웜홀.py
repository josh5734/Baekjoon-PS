import heapq

def show(graph):
    for i in range(len(graph)):
        for j in range(len(graph)):
            print(graph[i][j], end = ' ')
        print()

def dijkstra(start):
    q = []

    heapq.heappush(q, (0,start))   
    distance[start] = 0 

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue
    
        for i in range(1,n+1):
            cost = dist + graph[now][i]

            if cost < distance[i]:
                distance[i] = cost
                heapq.heappush(q,(cost, i))

def dfs(start):
    visited[start] = True
    for node in range(1, n+1):
        next = graph[start][node]
        if next != inf and not visited[node]:
            dfs(node)
    


tc = int(input())
inf, start = int(1e9), 1
for _ in range(tc):
    # 정점 개수, 간선 개수, 웜홀 개수
    n, m, w = map(int, input().split())
    answer = "NO" 

    # 각 정점 사이 거리를 배열 형태로 만들기
    graph = [[inf] * (n+1) for _ in range(n+1)]
    
    distance = [inf] * (n+1)

    # 모든 간선 정보 입력받기
    for _ in range(m):
        start, end, cost = map(int, input().split())
        if graph[start][end] > cost:
            graph[start][end] = cost
        if graph[end][start] > cost:
            graph[end][start] = cost
    
    # 웜홀은 무조건 가중치를 갱신해준다.
    for _ in range(w):
        start, end, cost = map(int, input().split())
        graph[start][end] = -cost





    # 어떤 두 지점을 순환하면 시간이 줄어들고, 
    # 두 지점에서 시작지점으로 갈 수만 있으면 가능
    visited = [False] * (n+1)
    dfs(1)
    for i in range(1,n+1):
        for j in range(1, n+1):
            if graph[i][j] + graph[j][i] < 0:
                if visited[i] == True or visited[j] == True:
                    answer = "YES"
                    break



    # 어느 지점에서 X라는 지점까지 최단거리로 가서
    # X 지점에서 원점으로 돌아올 때 웜홀이 그것을 상쇄한다면 가능
    dijkstra(1)
    print(distance)
    for i in range(1, n+1):
        if distance[i] + graph[i][1] < 0:
            answer = "YES"


    print(answer)

