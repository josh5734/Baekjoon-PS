from collections import deque

def isValidSection(graph,x,y):
    n = len(graph)
    if 0 <= x < n and 0 <= y < n:
        return True
    return False

def bfs(graph, x, y, dest_x, dest_y):
    q = deque()
    q.append((x, y))

    while q:
        curr_x, curr_y = q.popleft()
        # 8 가지 방향으로 이동 확인
        for i in range(8):
            next_x, next_y = curr_x + dx[i], curr_y + dy[i]
            # 그래프 안에 존재하고, 0인 칸에 대해서 이동
            if isValidSection(graph, next_x, next_y) and graph[next_x][next_y] == 0:
                q.append((next_x, next_y))
                graph[next_x][next_y] = graph[curr_x][curr_y] + 1
                # 목적지에 도착하면 이동 횟수를 리턴
                if next_x == dest_x and next_y == dest_y:
                    return graph[next_x][next_y] - 1

tc = int(input())
dx, dy = [2,2,1,1,-1,-1,-2,-2], [1,-1,2,-2,2,-2,1,-1] # 나이트가 움직일 수 있는 방향

for _ in range(tc):
    length = int(input())
    
    # 그래프, 현재 위치, 도착 위치 입력
    graph = [[0] * length for _ in range(length)]
    curr_x, curr_y = map(int, input().split())
    dest_x, dest_y = map(int, input().split())
    
    # 시작 위치를 1로 표시
    graph[curr_x][curr_y] = 1

    if curr_x == dest_x and curr_y == dest_y:
        print(0)
    else:
        print(bfs(graph, curr_x, curr_y, dest_x, dest_y))

    