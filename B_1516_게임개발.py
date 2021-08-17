from collections import deque
import sys


def topoloy_sort():

    q = deque()

    # 진입 차수가 0인 노드부터 큐에 넣고 시작
    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append(i)
            result[i] += time[i]

    # 모든 노드에 대해서 방문
    for i in range(1, n + 1):
        # 시작 노드를 큐에서 빼고 result에 기록
        start = q.popleft()

        # 시작 노드로부터 연결된 지점에 대해서
        for j in graph[start]:
            end = j
            result[j] = max(result[j], result[start] + time[j])
            # 간선을 삭제하며 진입차수를 감소시킴
            indegree[end] -= 1
            # 만약 진입차수가 0이 되는 노드가 생기면 다시 큐에 삽입
            if indegree[end] == 0:
                q.append(end)

    # 결과 출력
    for i in range(1, n + 1):
        print(result[i])


if __name__ == "__main__":
    # 건물의 수
    n = int(input())

    # 시간 정보를 담을 리스트
    time = [0] * (n+1)

    # 필요한 시간 결과를 담을 리스트
    result = [0] * (n + 1)
    # 진입차수를 기록할 리스트
    indegree = [0] * (n + 1)

    # 간선 정보를 담을 그래프
    graph = [[] for _ in range(n+1)]
    for i in range(1, n + 1):
        line = list(map(int, sys.stdin.readline().split()))
        # indegree가 0인 경우
        if len(line) == 2:
            time[i] += line[0]
        else:
            time[i] += line[0]
            # 먼저 지어져야 할 건물들에 대해 정보 담기
            for pre in line[1:-1]:
                indegree[i] += 1
                graph[pre].append(i)

    topoloy_sort()
