# dp[i][j] = _ _ _ _ _ ... _ _  j개의 수로 i를 만드는 경우의 수
# dp[i][j] = 맨 앞에 0이 오는 경우, 1이 오는 경우,..., i-1, i가 오는 경우
# --> dp[i][j] = dp[i][j-1] + dp[i-1][j-1] + dp[i-2][j-1] + .... + dp[1][j-1] + dp[0][j-1]
# --> dp[i][j-1] = dp[i][j-2] + dp[i-1][j-2] + dp[i-2][j-2] + .... + dp[1][j-2] + dp[0][j-2]
# ...
def recursivelySolve(i, j):
    if j == 1:
        return dp[i][j]
    else:
        for x in range(i+1):
            dp[i][j] += dp[i-x][j-1]

n, k = map(int, input().split())

dp = [[0] * 201 for _ in range(201)]
for i in range(1,201):
    dp[i][1] = 1

for i in range(201):
    for j in range(1, 201):
        recursivelySolve(i,j)
print(dp[n+1][k] % 1000000000)

