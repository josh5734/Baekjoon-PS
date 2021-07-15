
def find_path(last, visited):
    if visited == VISITED_ALL:
        return graph[last][0] or INF

    # cache[last][visited] --> last 지점에서 visited 지점을 방문한 적이 있는가?
    if cache[last][visited] is not None:
        return cache[last][visited]
        
    tmp = INF        
    for city in range(n):
        # visited & (1 < city) == 0 : 아직 방문하지 않은 도시 중에
        # graph[last][city] != 0: 길이 있다면
        # tmp를 tmp와 다른 도시들까지 최소 거리 + 지금 도시에서 다른 도시까지 거리 중 작은 값으로 갱신한다.
        if visited & (1 << city) == 0 and graph[last][city] != 0:
            tmp = min(tmp,
            find_path(city, visited | (1 << city)) + graph[last][city])
    cache[last][visited] = tmp
    return tmp

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

cache = [[None] * (1 << n) for _ in range(n)]
INF = float('inf')
VISITED_ALL = (1 << n) - 1
answer = find_path(0, 1 << 0)  
print(answer)