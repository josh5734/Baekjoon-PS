import heapq as hq
import sys


def findMST():
    pq = []  # 우선순위 큐를 통해 최소간선 먼저 pop
    hq.heappush(pq, (0, 1))  # 비용 0, 1번 정점 삽입
    count = 0
    answer = 0
    while count < v:
        cost, start = hq.heappop(pq)
        if not visited[start]:  # 방문하지 않은 정점에 대해
            visited[start] = True
            answer += cost
            count += 1

            for end, cost in graph[start]:  # 모든 이어진 간선을 큐에 삽입
                hq.heappush(pq, (cost, end))
    return answer


if __name__ == "__main__":
    v, e = map(int, input().split())
    graph = [[] for _ in range(v+1)]
    for _ in range(e):  # 간선 정보 입력받기
        start, end, cost = map(int, sys.stdin.readline().split())
        graph[start].append((end, cost))
        graph[end].append((start, cost))

    visited = [False] * (v+1)  # 방문 체크
    answer = findMST()
    print(answer)
