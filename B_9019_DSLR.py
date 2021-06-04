from collections import deque

def bfs(start, ops):
    q = deque()
    q.append((start,ops))
    visited[int(start)] = True
    
    count = 0
    while q:
        count += 1
        curr_number_str, curr_step = q.popleft()
        curr_number = int(curr_number_str)
        if curr_number == int(end):
            return curr_step

        next_D = str(curr_number * 2) if curr_number * 2 <= 9999 else str((curr_number * 2) % 10000)
        next_S = str(curr_number -1) if curr_number > 0 else str(9999)
        next_L = curr_number_str[1:] + curr_number_str[0]
        next_R = curr_number_str[-1] + curr_number_str[:-1]
        # 레지스터 네 자리 만들기
        while(len(next_D) < 4):
            next_D = '0' + next_D

        while(len(next_S) < 4):
            next_S = '0' + next_S

        if not visited[int(next_D)]:
            q.append((str(next_D), curr_step+"D"))
            visited[int(next_D)] = True
        if not visited[int(next_S)]:
            q.append((str(next_S), curr_step+"S"))
            visited[int(next_S)] = True
        if not visited[int(next_L)]:
            q.append((next_L, curr_step+"L"))
            visited[int(next_L)] = True
        if not visited[int(next_R)]:
            q.append((next_R, curr_step+"R"))
            visited[int(next_R)] = True



tc = int(input())

for _ in range(tc):
    start, end = input().split()
    # 레지스터 네 자리 만들기
    while(len(start) < 4):
        start = '0' + start
    visited = [False] * 10000
    print(bfs(start,""))

