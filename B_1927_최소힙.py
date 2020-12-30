import sys
import heapq


if __name__ == "__main__":
    # 연산의 개수, 사용할 힙
    n = int(input())
    h = []

    for _ in range(n):
        number = int(sys.stdin.readline())
        if number == 0:
            if not h:
                print(0)
            else:
                print(heapq.heappop(h))
        else:
            heapq.heappush(h, number)
