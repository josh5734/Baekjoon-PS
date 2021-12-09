import sys
sys.setrecursionlimit(10 ** 9)
input = sys.stdin.readline

def boundChk(x, y, n, m):
    return 0 <= x < n and 0 <= y < m

def bitExpression(k):
    return bin(int(k))[2:].zfill(4)

def dfs(x, y, visited, room):
    room.append((x,y))
    visited[x][y] = True
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        # 바운드 체크, 성곽 체크
        if 0 <= nx < m and 0 <= ny < n and boundary[x][y][i] == '0':
            # 이미 방문하지 않았다면
            if not visited[nx][ny]:
                dfs(nx,ny, visited, room)

n, m = map(int, input().split())

# 각 지점에서 상하좌우에 벽이 있는지를 비트형태로 표현
boundary = [list(map(bitExpression, input().split())) for _ in range(m)]
# 남쪽 = 8, 동쪽 = 4, 북쪽 = 2, 서쪽 = 1
dx, dy = [1,0,-1,0],[0,1,0,-1]

rooms = []
visited = [[False] * n for _ in range(m)]
for i in range(m):
    for j in range(n):
        if not visited[i][j]:
            room = []
            dfs(i,j, visited, room)
            rooms.append(room)     

# 방 크기를 기준으로 오름차순 정렬
rooms = sorted(rooms, key = lambda x : len(x))
numOfRooms = len(rooms) # 방의 개수
maxRoomArea = len(rooms[-1]) # 가장 큰 방
maxRoomAreaByBreakingWall = len(rooms[-1])

# 벽 하나를 뚫었을 때 가장 큰 방의 크기 구하기
for i in range(numOfRooms):
    for j in range(i+1,numOfRooms):
        for x, y in rooms[i]:
            for d in range(4):
                nx, ny = x + dx[d], y + dy[d]
                # 옆 칸에 있으면 방을 합칠 수 있음
                if 0 <= nx < m and 0 <= ny < n and (nx, ny) in rooms[j]:
                            areaTotal = len(rooms[i]) + len(rooms[j])
                            if areaTotal > maxRoomAreaByBreakingWall:
                                maxRoomAreaByBreakingWall = areaTotal
                                break
print(numOfRooms)
print(maxRoomArea)
print(maxRoomAreaByBreakingWall)