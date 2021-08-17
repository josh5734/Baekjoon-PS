import sys
from collections import deque

def bfs(start):
    q = deque()
    q.append(start)
    # 시작점을 0으로 설정
    kevin_num_list[start][start] = 0
    while q:
        now = q.popleft()
        for next in graph[now]:
            # 현재 지점에서 갈 수 있는 곳 중에서 방문하지 않은 곳(= -1) 방문
            if kevin_num_list[start][next] == -1:
                q.append(next)
                # 방문을 하면서 거리를 갱신
                kevin_num_list[start][next] = kevin_num_list[start][now] + 1
    
    # 최종적으로 케빈 베이컨 수의 합을 계산해서 리스트에 출발 유저의 번호와 함께 저장
    kevin_number.append([start,sum(kevin_num_list[start][1:])])

# 유저의 수, 관계의 수
n, m = map(int, input().split())

# 친구 관계를 나타내는 인접 리스트
graph = [[] for _ in range(n+1)]
for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

# 처음에 다 -1로 초기화하고 bfs 수행
kevin_num_list = [[-1] * (n+1) for _ in range(n+1)]
kevin_number = []

# 각 사람의 케빈 베이컨 수를 구하기
for i in range(1,n+1):
    bfs(i)

# 케빈 베이컨 수가 작은 것부터 오름차순으로 정렬
kevin_number.sort(key = lambda x : x[1])
# 가장 작은 녀석을 바로 출력
print(kevin_number[0][0])

        

