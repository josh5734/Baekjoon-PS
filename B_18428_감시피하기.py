import sys
import copy
from itertools import combinations as C

def detect(x, y):
    studentDetection = False
    for i in range(4):
        further = 1
        while True:  # 상하좌우로 끝까지 탐색
            nx, ny = x + further * dx[i], y + further * dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if testGraph[nx][ny] == 'S':  # 학생을 볼 수 있으면 True
                    studentDetection = True
                elif testGraph[nx][ny] == 'O':  # 장애물 만나면 다른 방향 전환
                    break
                further += 1
            else:  # 범위에서 벗어나면 다른 방향 전환
                break
    return studentDetection

if __name__ == "__main__":
    n = int(input())
    graph = []
    for _ in range(n):
        graph.append(list(sys.stdin.readline().split()))

    blank = []  # 벽을 설치할 수 있는 후보 공간
    for i in range(n):
        for j in range(n):
            if graph[i][j] == 'X':
                blank.append((i, j))

    dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
    newObstacles = list(C(blank, 3))  # 벽을 3개 세울 수 있는 모든 조합
    answer = "NO"
    for o in newObstacles:
        testGraph = copy.deepcopy(graph)
        for x, y in o:
            testGraph[x][y] = 'O'
        canHide = True
        for i in range(n):
            for j in range(n):
                if testGraph[i][j] == 'T':
                    if detect(i, j) == True:  # 한 학생이라도 잡히면 실패
                        canHide = False
        if canHide:  # 하나의 경우에서라도 숨을 수 있는 경우가 생기면 answer = "YES"로 변경
            answer = "YES"
    print(answer)
