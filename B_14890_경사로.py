import sys
input = sys.stdin.readline

def isValidWay(line, graph):
    used = [False] * n # 경사로 건설 여부를 위한 리스트
    row = graph[line] # 현재 확인할 길 
    for i in range(n-1):
        # 높이가 다른 곳 발견        
        if row[i] != row[i+1]:
            # 높이가 2차이 이상 나면 실패
            if abs(row[i] - row[i+1]) >= 2:
                return False
            else:
                # 높은 곳에서 낮은 곳이면 그 이후를 관찰
                if row[i] == row[i+1] + 1:
                    # 순서대로 범위 초과, 지그재그, 이미 경사로 설치 확인
                    if i + l >= n: return False
                    if len(set(row[i+1:i+1+l])) != 1: return False
                    if any(used[i+1:i+1+l]): return False
                    for j in range(i+1, i+l+1):
                        used[j] = True
                # 낮은 곳에서 높은 곳이면 그 이전을 관찰
                elif row[i] == row[i+1] - 1:
                    if (i+1) - l < 0 : return False
                    if len(set(row[i+1-l:i+1])) != 1: return False
                    if any(used[i+1-l:i+1]): return False
                    for j in range(i+1-l, i+1):
                        used[j] = True

    return True

n, l = map(int, input().split())
row_graph = [list(map(int, input().split())) for _ in range(n)] # 행 탐색을 위한 그래프
col_graph = list(zip(*row_graph)) # 열 탐색을 위한 그래프
answer = 0

for line in range(n):
    if isValidWay(line, row_graph):
        answer += 1
    if isValidWay(line, col_graph):
        answer += 1
print(answer)

    
