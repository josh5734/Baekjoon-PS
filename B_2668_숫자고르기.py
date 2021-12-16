n = int(input())
arr = [0] + [int(input()) for _ in range(n)]
visited = [False] * (n+1)

for i in range(1, n+1):
    temp = set() # i번에서 출발하여 깊이 우선 탐색을 통해 도달할 수 있는 집합
    curr = i # curr를 시작 노드점 번호로 지정
    if not visited[curr]: 
        while True:
            next = arr[curr]
            if next not in temp:
                temp.add(next)
                curr = next
                if next == i: # 다음 노드가 시작 노드라면 싸이클 생성
                    for t in temp: visited[t] = True
                    break
            else: # 이미 방문한 곳을 방문하면 종료
                break                      

print(visited.count(True))
for i in range(1, n+1):
    if visited[i] == True: print(i)