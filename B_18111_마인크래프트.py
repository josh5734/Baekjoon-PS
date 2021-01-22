import sys
from collections import Counter

if __name__ == "__main__":
    n, m, b = map(int, input().split())

    min_height, max_height = 500, 0
    graph = []
    max_block = b
    for _ in range(n):
        line = map(int, sys.stdin.readline().split())
        graph += line
    max_block += sum(graph)
    # 높이를 기준으로 땅을 묶기
    graph_height = dict(Counter(graph))
    min_time = int(1e20)
    max_height = 0
    # 균형잡힌 높이는 최소높이 0에서 최대높이 257까지임
    for h in range(257):
        if max_block >= h * n * m:
            time = 0
            for height in graph_height:
                if height < h:
                    time += 1 * (h - height) * graph_height[height]
                elif height > h:
                    time += 2 * (height - h) * graph_height[height]

            if time <= min_time:
                min_time = time
                max_height = h
    print(min_time, max_height)
