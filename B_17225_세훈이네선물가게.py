from collections import deque
import sys

if __name__ == "__main__":
    a, b, n = map(int, input().split())

    # 전체 주문에 대한 정보
    orders = []

    # 상민, 지수가 포장한 선물들
    sangmin, zisu = [], []
    # 상민, 지수의 시간
    t1, t2 = 0, 0
    for _ in range(n):
        line = list(sys.stdin.readline().split())
        t, color, order = int(line[0]), line[1], int(line[2])
        # 각 선물의 포장을 시작하는 시간을 큐에 삽입
        if color == 'B':
            if t >= t1:
                for i in range(order):
                    orders.append((t + i * a, 'B'))
                t1 = t + order * a
            else:
                for i in range(order):
                    orders.append((t1 + i * a, 'B'))
                t1 = t1 + order * a
        elif color == 'R':
            if t >= t2:
                for i in range(order):
                    orders.append((t + i * b, 'R'))
                t2 = t + order * b
            else:
                for i in range(order):
                    orders.append((t2 + i * b, 'R'))
                t2 = t2 + order * b

    orders = sorted(orders)
    cnt = 0
    number = len(orders)
    while orders:
        item = orders.pop()
        if item[1] == 'B':
            sangmin.insert(0, number-cnt)
        else:
            zisu.insert(0, number-cnt)
        cnt += 1

    print(len(sangmin))
    for x in sangmin:
        print(x, end=' ')
    print()
    print(len(zisu))
    for x in zisu:
        print(x, end=' ')
    print()
