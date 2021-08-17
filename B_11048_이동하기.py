import sys

n, m = map(int, input().split())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

# dp[i][j] = (i,j) 에서 사탕 누적 개수 최대값
dp = [[0] * (m+1) for _ in range(n+1)]  # Indexing 편의를 위해 테두리는 0으로 초기화
dp[1][1] = graph[0][0]

for i in range(1, n+1):
    for j in range(1, m+1):
        # 위에서 아래로 오는 경우, 왼쪽에서 오른쪽으로 오는 경우
        dp[i][j] = max(dp[i-1][j], dp[i][j-1]) + graph[i-1][j-1]

print(dp[n][m])