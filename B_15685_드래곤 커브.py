import sys
input = sys.stdin.readline
n = int(input())
answer = 0
points = [[False] * 101 for _ in range(101)] # 드래곤 커브가 지나가는 좌표들
dx, dy = [1, 0, -1, 0], [0, -1, 0, 1] # 0,1,2,3 방향
for _ in range(n):
    preGen = []
    x, y, direction, generation = map(int, input().split())
    # 0 세대의 드래곤 커브 추가
    preGen = [(x,y), (x + dx[direction], y + dy[direction])]
    points[x][y] = True
    points[x+dx[direction]][y+dy[direction]] = True
    while generation > 0:
        generation -= 1
        last_x, last_y = preGen[-1] # 이전 세대의 끝점
        newGen = []
        for x, y in preGen[:-1][::-1]:
            # 이전 세대의 드래곤 커브를 끝점을 기준으로 90도 회전
            nx, ny = (y - last_y) * (-1) + last_x, (x - last_x) + last_y
            points[nx][ny] = True
            newGen.append((nx,ny))
        preGen.extend(newGen)
for i in range(100):
    for j in range(100):
        if all([points[i][j], points[i][j+1], points[i+1][j], points[i+1][j+1]]):
            answer += 1

print(answer)

