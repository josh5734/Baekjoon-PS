# dp[i][j] = i개의 완전한 알약, j개의 반절짜리 약이 남았을 때 조합의 수
dp = [[0] * 31 for _ in range(31)]
for i in range(1, 31): # 반알짜리만 남아있으면 일렬로 나열
    dp[0][i] = 1

for i in range(1, 31):
    for j in range(30):
        if j == 0: # 완전한 알약 하나를 먹으면 반절짜리 알약이 하나 생긴다.
            dp[i][j] = dp[i-1][j+1]
        else: # 반절짜리 약을 하나 먹은 상황 + 완전한 알약 하나를 먹은 상황
            dp[i][j] = dp[i][j-1] + dp[i-1][j+1]
# 결과 출력           
while True:
    n = int(input())
    if n == 0: break
    print(dp[n][0]) # 결과 : n개의 완전한 알약이 있을 때 경우의 수
