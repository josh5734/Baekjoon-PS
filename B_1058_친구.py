from collections import deque
import sys

def bfs(start):
    visited = [0] * n
    q = deque()
    q.append([start, 0])
    while q:
        curr, count = q.popleft()
        for friend in graph[curr]:
            if not visited[friend]:
                if count <= 1:
                    visited[friend] = 1
                    q.append((friend, count+1))

    return visited

n = int(input())

# 각 사람의 친구를 나타내는 그래프
graph = [[] for _ in range(n)]

# 친구 관계를 인접리스트 형태로 입력받는다.
for i in range(n):
    line = sys.stdin.readline().rstrip()
    for j in range(n):
        if line[j] == 'Y':
            graph[i].append(j)

answer = 0
# 2-친구가 되려면 직접 연결 Or 한 다리 건너 연결
for i in range(n):
    friends = bfs(i)
    numberOfTwoFriends = friends.count(1) - 1
    if numberOfTwoFriends > answer:
        answer = numberOfTwoFriends
print(answer)