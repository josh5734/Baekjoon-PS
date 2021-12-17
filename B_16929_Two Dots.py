import sys
input = sys.stdin.readline

def findEdgeDir(inDir): # 들어오는 간선 방향을 나가는 방향 기준으로 변환
    outDir = -1
    if inDir == 0:
        outDir = 1
    elif inDir == 1:
        outDir = 0
    elif inDir == 2:
        outDir = 3
    else:
        outDir = 2
    return outDir
    
# 시작 노드와 연결된 간선을 기준으로 중복 방문 없이 다시 올 수 있는가?
def checkCycle(x, y, startX, startY, visitedNode, visitedEdge):
    visitedNode[x][y] = True
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < n and 0 <= ny < m: # 범위 체크
            if dots[nx][ny] != dots[x][y]: continue # 같은 모양 체크
            
            if nx == startX and ny == startY: # 시작 노드로 돌아오는 경우
                edgeDir = findEdgeDir(i)
                if not visitedEdge[edgeDir]:
                    return True
            else: # 일반적인 경우 - 다른 노드로 이동하는 경우
                if not visitedNode[nx][ny]:
                    visitedNode[nx][ny] = True
                    if x == startX and y == startY: # 시작 노드에서 나갈 때만 간선에 방문 체크
                        visitedEdge[i] = True
                    if checkCycle(nx, ny, startX, startY, visitedNode, visitedEdge):
                        return True
    return False
                    

n, m = map(int, input().split())
dots = [list(input().rstrip()) for _ in range(n)]
dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
isCycle = False
for i in range(n):
    for j in range(m):
        visitedNode = [[False] * m for _ in range(n)] # 각 노드의 방문 여부
        visitedEdge = [False] * 4 # 시작 노드에서 가질 수 있는 간선 네 개의 방문 여부
        if checkCycle(i, j, i, j, visitedNode, visitedEdge):
            isCycle = True
print("Yes") if isCycle else print("No")