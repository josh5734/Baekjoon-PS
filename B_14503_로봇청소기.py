import sys
def dfsCleaner(r,c, direction):
    global count
    # 2. 왼쪽 방향에 아직 청소하지 않은 공간이 존재하면, 그 방향으로 회전하고 다음 한 칸을 전진하고 구역 청소
    leftDirection = (direction + 3) % 4
    nr, nc = r + dr[leftDirection], c + dc[leftDirection]
    if graph[nr][nc] == 0: # 왼쪽에 청소를 하지 않은 공간이 있으면
        graph[nr][nc] = -1 # 청소를 하고
        count += 1 # 청소를 한 구역 수 증가
        dfsCleaner(nr,nc,leftDirection) # 반복 수행 
    
    else: # 왼쪽에 청소를 할 공간이 없으면        
        temp = 0
        for i in range(4):
            nr, nc = r+dr[i], c+dc[i]
            if graph[nr][nc] == -1 or graph[nr][nc] == 1: 
                temp += 1 
        if temp == 4: # 네 방향이 모두 청소가 되어있거나 벽일 때
            if graph[r-dr[direction]][c-dc[direction]] == 1: # 뒤쪽 방향이 벽이면
                return; # 종료
            else:
                dfsCleaner(r-dr[direction],c-dc[direction],direction) # 한 칸 후진하고 다시 수행
        else: # 위 경우가 아니면 그냥 그 자리에서 왼쪽으로 돌아서 다시 수행
            dfsCleaner(r,c,leftDirection) 

if __name__ == "__main__":
    n, m = map(int, input().split())
    r, c, direction = map(int, input().split())
    graph = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]

    dr, dc = [-1,0,1,0],[0,1,0,-1] # 북동남서 순서
    graph[r][c] = -1 # 맨 처음 위치 청소
    count = 1
    dfsCleaner(r,c,direction) # 남은 곳 청소 시작
    print(count)