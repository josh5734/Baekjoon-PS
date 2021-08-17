import heapq
import sys

if __name__ == "__main__":
    n = int(input())

    # 몇 번째 큰 수인지 확인하는 변수
    count = 0
    # 가장 큰 원소를 가져올 max heap
    q = []

    for i in range(n):
        line = list(map(int, sys.stdin.readline().split()))
        q.extend(line)
        heapq.heapify(q)
        while(len(q) > n):
            heapq.heappop(q)

    print(heapq.heappop(q))
