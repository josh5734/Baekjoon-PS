from collections import defaultdict, deque
import sys


# bfs로 끝 정점까지 거리 구하기
def getDistance(start):
    randomNode, maxDistance = 0,  0
    visited = [False] * (v+1)
    visited[start] = True
    q = deque()
    q.append((start, 0))

    while q:
        currNode, distance = q.popleft()

        if maxDistance < distance:
            maxDistance = distance
            randomNode = currNode

        for childNode, dist in tree[currNode]:
            if not visited[childNode]:
                visited[childNode] = True
                q.append((childNode, distance + dist))

    return randomNode, maxDistance

v = int(input())

# 트리 정보 입력받기
tree = defaultdict(list)
for _ in range(v):
    line = list(map(int, sys.stdin.readline().split()))
    parent = line[0]
    for i in range(1, len(line)-1, 2):
        child, dist = line[i], line[i+1]
        tree[parent].append((child, dist))

# 트리의 지름 구하기
# 1. 트리에서 임의의 정점 x를 찾는다.
# 2. 정점 x에서 가장 먼 정점 y를 찾는다.
# 3. 정점 y에서 가장 먼 정점 z를 찾는다.
randomNode, maxDistance = getDistance(1)
randomNode, maxDistance = getDistance(randomNode)
print(maxDistance)