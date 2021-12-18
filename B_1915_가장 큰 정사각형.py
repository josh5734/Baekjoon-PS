import sys
input = sys.stdin.readline
n, m = map(int, input().split())
answer = 0
grid = [list(map(int, input().rstrip())) for _ in range(n)]

# dp[i][j] = (i,j)위치에서 자신을 왼쪽 아래 모서리로 하는 정사각형 길이를 저장
dp = [[0] * (m+1) for _ in range(n+1)] # 테두리는 0으로 초기화

for i in range(1, n+1):
    for j in range(1, m+1):
        # 현재 위치가 0이라면 정사각형 만들 수 없음
        if grid[i-1][j-1] == 0: continue
        else:
            dp[i][j] = min(dp[i-1][j-1], dp[i][j-1], dp[i-1][j]) + 1
            answer = max(answer, dp[i][j])
print(answer ** 2)