import sys
from collections import deque
from itertools import product

input = sys.stdin.readline


unwatched = 0
answer = 100000
n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
camera = []
for i in range(n):
    for j in range(m):
        # 카메라의 위치와 어떤 종류의 카메라인지를 기록
        if 1 <= graph[i][j] <= 5:
            camera.append((i,j, graph[i][j], []))
        elif graph[i][j] == 0:
            unwatched += 1


# 각 감시카메라의 관찰 방향
cam1_direction = [[[-1,0]],[[1,0]],[[0,-1]],[[0,1]]]
cam2_direction = [[[-1,0],[1,0]],[[0,-1],[0,1]]]
cam3_direction = [[[-1,0],[0,-1]], [[-1,0],[0,1]], [[1,0],[0,-1]], [[1,0],[0,1]]]
cam4_direction = [[[-1,0],[1,0],[0,-1]], [[-1,0],[1,0],[0,1]], [[-1,0],[0,-1],[0,1]],[[1,0],[0,-1],[0,1]]]
cam5_direction = [[[-1,0],[1,0],[0,-1],[0,1]]]


def checkArea(camera_direction, cam):
    for direction in camera_direction:
        area = []
        for d in direction:
            q = deque()
            q.append((x,y))
            while q:
                ax, ay = q.popleft()
                nx, ny = ax + d[0], ay + d[1]
                if 0 <= nx < n and 0 <= ny < m:
                    if graph[nx][ny] == 6:
                        break
                    else:
                        q.append((nx,ny))
                        if graph[nx][ny] == 0:
                            area.append((nx,ny))
        cam[3].append(area)

# 각 카메라별로 감시할 수 있는 구간을 기록해본다
for cam in camera:
    x, y, type = cam[0], cam[1], cam[2]
    if type == 1:
        checkArea(cam1_direction, cam)
    elif type == 2:
        checkArea(cam2_direction, cam)
    
    elif type == 3:
        checkArea(cam3_direction, cam)
    
    elif type == 4:
        checkArea(cam4_direction, cam)
    
    elif type == 5:
        checkArea(cam5_direction, cam)

area_list = []
for cam in camera:  
    area_list.append(cam[3])

area_comb = list(product(*area_list))
for area in area_comb:
    checked = set()
    for a in area:
        for x, y in a:
            checked.add((x,y))
    if answer > unwatched - len(checked):
        answer = unwatched - len(checked)
print(answer)

