import sys
import copy

########pypy########


def spread_in(x, y):
    # 주변에서 들어오는 미세먼지
    temp = 0
    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if nx >= 0 and ny >= 0 and nx < r and ny < c:
            if room[nx][ny] != -1:
                temp += (room[nx][ny] // 5)
    return temp


def spread_out(x, y):
    temp = 0
    direction = 0
    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if nx >= 0 and ny >= 0 and nx < r and ny < c:
            if room[nx][ny] != -1:
                direction += 1

    temp += (room[x][y]//5) * direction
    return temp


if __name__ == "__main__":
    r, c, t = map(int, input().split())
    # 공기청정기의 위치 파악
    cleaner = 0
    room = []
    for i in range(r):
        line = list(map(int, sys.stdin.readline().split()))
        if line[0] == -1:
            cleaner = i
        room.append(line)

    dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
    for _ in range(t):
        new_room = copy.deepcopy(room)
        # 미세먼지 확산
        for i in range(r):
            for j in range(c):
                if room[i][j] != -1:
                    dirty = (spread_in(i, j) - spread_out(i, j))
                    new_room[i][j] += dirty

        # 반시계방향 공기청정기
        room[cleaner-1][1] = 0
        for i in range(2, c):
            room[cleaner-1][i] = new_room[cleaner-1][i-1]

        for i in range(cleaner-1):
            room[i][-1] = new_room[i+1][-1]

        for i in range(c-1):
            room[0][i] = new_room[0][i+1]

        for i in range(1, cleaner-1):
            room[i][0] = new_room[i-1][0]

        for i in range(1, cleaner-1):
            for j in range(1, c-1):
                room[i][j] = new_room[i][j]

        # 시계방향 공기청정기
        room[cleaner][1] = 0
        for i in range(2, c):
            room[cleaner][i] = new_room[cleaner][i-1]

        for i in range(cleaner+1, r):
            room[i][-1] = new_room[i-1][-1]

        for i in range(c-1):
            room[r-1][i] = new_room[r-1][i+1]

        for i in range(cleaner+1, r-1):
            room[i][0] = new_room[i+1][0]

        for i in range(cleaner+1, r-1):
            for j in range(1, c-1):
                room[i][j] = new_room[i][j]

    answer = 0
    for i in range(r):
        for j in range(c):
            if room[i][j] != -1:
                answer += room[i][j]
    print(answer)
