from collections import deque
import sys
input = sys.stdin.readline

def bfs(start, group):
    q = deque()
    q.append((start, 1)) # 시작 지점과 해당 지점의 그룹번호
    group[start] = 1

    while q:
        curr, currGroup = q.popleft()
        for adj in graph[curr]:
            if group[adj] == 0:
                # 방문 표시를 하고 반대 그룹에 편성
                group[adj] = -currGroup
                q.append((adj, -currGroup))
            else:
                # 이미 방문을 한 정점이 같은 그룹에 있는지 확인
                if group[adj] == currGroup:
                    return False
    return True

k = int(input())
for _ in range(k):
    v, e = map(int, input().split())
    graph = [[] for _ in range(v+1)]
    for _ in range(e):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    group = [0]* (v+1) # 각 정점들이 속한 그룹을 담는 배열
    answer = "YES"
    for i in range(1, v+1):
        if group[i] == 0:
            if not bfs(i, group):
                answer = "NO"
                break
    print(answer)