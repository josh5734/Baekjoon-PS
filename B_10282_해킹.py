import sys, heapq
input = sys.stdin.readline
inf = int(1e9)

def dijkstra(graph, start):
    # 각 컴퓨터가 감염되기까지 걸리는 최단 시간을 기록하는 리스트
    time = [inf] * (n+1)
    time[start] = 0

    # 감염되는 컴퓨터의 개수, 마지막 컴퓨터가 감염되기까지 걸리는 시간
    count, endTime = 0, 0

    pq = []
    heapq.heappush(pq, (0, start))
    while pq:
        curr_time, curr_computer = heapq.heappop(pq)
        if curr_time < time[curr_computer]:
            continue
    
        for next in graph[curr_computer]:
            next_time, next_computer = next[0], next[1]
            # 최단 시간 갱신
            if curr_time + next_time < time[next_computer]:
                time[next_computer] = curr_time + next_time
                heapq.heappush(pq, (curr_time + next_time, next_computer))
    
    for t in time:
        if t < inf:
            count +=1
            # 마지막 컴퓨터가 감염되는 시간
            if t > endTime:
                endTime = t

    return count, endTime


# 테스트 케이스의 개수
tc = int(input())

for _ in range(tc):
    # 컴퓨터 개수, 의존성 개수, 해킹당한 컴퓨터 번호
    n, d, c = map(int, input().split())
    
    graph = [[] for _ in range(n+1)]
    for _ in range(d):
        a, b, s = map(int, input().split())
        graph[b].append((s, a))
    
    count, endTime = dijkstra(graph, c)
    print(count, endTime)
