import sys
from collections import deque
def bfs(begin, end, mid):
    q = deque()
    q.append((begin, 0))
    visited[begin] = True
    while q:
        curr, weight = q.popleft();
        if curr == end: # 현재 값이 도착지라면 True
            return True
        for next, weight in graph[curr]:
            # mid값보다 현재 무게가 더 클때만 이동 가능
            if not visited[next] and weight >= mid:
                q.append((next,weight))    
                visited[next] = True # 넣으면서 방문 체크
    return False

# 이분탐색 - bfs를 수행
if __name__ == "__main__":
    n, m = map(int, input().split())   
    graph = [[] for _ in range(n+1)]
    for _ in range(m): # adj-list 형태로 graph 입력
        start, dest, weight = map(int, sys.stdin.readline().split())
        graph[start].append((dest,weight))
        graph[dest].append((start,weight))
    begin, end = map(int, input().split())
    left, right = 1, int(10e9)
    answer = 0
    while left <= right:
        visited = [False] * (n+1)   # visited 초기화
        mid = (left + right) // 2
        # bfs == True이면, 주어진 mid보다 같거나 큰 무게로 
        # 시작지점부터 도착지점까지 이동할 수 있음
        if bfs(begin, end, mid) == True: 
            left = mid + 1
            answer = mid
        else:
            right = mid - 1

    print(answer)
