import sys
from collections import deque
from itertools import combinations as cb


def chicken_distance(x, y, dest):
    min_dist = 200
    for c in dest:
        cx, cy = c[0], c[1]
        dist = abs(cx-x)+abs(cy-y)
        if dist <= min_dist:
            min_dist = dist
    return min_dist


if __name__ == "__main__":
    # n, m 입력받기
    n, m = map(int, input().split())

    # 지도 정보, 집 위치 정보, 치킨 집이 주문을 받는 횟수
    graph, house, chicken = [], [], []
    for i in range(n):
        line = list(map(int, sys.stdin.readline().split()))
        graph.append(line)
        # 집의 위치만 따로 house 리스트에 담는다.
        for j in range(n):
            if line[j] == 1:
                house.append((i, j))
            if line[j] == 2:
                chicken.append((i, j))

    # 치킨집 M개를 뽑는 경우
    comb = list(cb(chicken, m))

    # M개를 뽑았을 때 도시의 치킨 거리
    ways = []

    for c in comb:
        total = 0
        for h in house:
            x, y = h[0], h[1]
            total += chicken_distance(x, y, c)
        ways.append(total)

    # 가장 짧은 거리 출력
    print(min(ways))
