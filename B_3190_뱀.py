from collections import deque
import sys
sys.setrecursionlimit(100000000)


def check(graph, headRow, headCol):
    n = len(graph)
    # 벽을 만나면 False
    if headRow < 0 or headRow >= n or headCol < 0 or headCol >= n:
        return False
    count = 0
    # 자기 자신의 몸을 만나면 False
    for i in range(len(snakeShape)-1):
        if [headRow, headCol] == snakeShape[i]:
            return False
    return True


def snakeTrip(snakeShape, direction, time):
    time += 1
    # 뱀의 마지막 몸통 부분의 길이를 늘려 머리를 추가
    bodyRow, bodyCol = snakeShape[-1][0], snakeShape[-1][1]
    headRow, headCol = bodyRow + dx[direction], bodyCol + dy[direction]
    if check(graph, headRow, headCol) == False:
        return time

    # 만약 이동한 칸에 사과가 있다면 그 칸에 사과를 없애고 꼬리 고정
    if graph[headRow][headCol] == 'A':
        graph[headRow][headCol] = 0
    # 만약 이동한 칸에 사과가 없다면 몸길이를 줄여서 꼬리가 위치한 칸을 없앤다.
    else:
        snakeShape.popleft()
    snakeShape.append([headRow, headCol])  # 머리 추가

    # 방향이 바뀐다면 머리 정보를 수정해준다.
    if len(directionChangeInfo) > 0 and time == directionChangeInfo[0][0]:
        changeDirection = directionChangeInfo[0][1]
        if changeDirection == 'D':
            direction = (direction + 1) % 4  # 시계방향
        elif changeDirection == 'L':
            direction = (direction + 3) % 4  # 반시계방향
        directionChangeInfo.popleft()
    return snakeTrip(snakeShape, direction, time)


if __name__ == "__main__":
    # 문제 정보 입력받기
    n = int(input())
    appleNumber = int(input())
    appleLocation = []
    for _ in range(appleNumber):
        appleLocation.append(list(map(int, input().split())))

    directionChangeNumber = int(input())
    directionChangeInfo = deque()
    for _ in range(directionChangeNumber):
        time, direction = input().split()
        directionChangeInfo.append([int(time), direction])

    # 그래프 정보 입력받기 / 뱀: 'S', 사과: 'A'로 표시 / (0,0)을 시작 기준으로 잡기
    graph = [[0] * n for _ in range(n)]
    graph[0][0] = 'S'
    for a in appleLocation:
        graph[a[0]-1][a[1]-1] = 'A'

    snakeShape = deque()  # 뱀의 꼬리, 몸통, 머리 정보들을 담는 큐  생성
    snakeShape.append([0, 0])
    # 오른쪽, 아래쪽, 왼쪽, 위쪽으로 방향 인덱스 설정 - 시계 방향
    dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
    direction, time = 0, 0
    answer = snakeTrip(snakeShape, direction, time)
    print(answer)
