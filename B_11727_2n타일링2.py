n = int(input())
dp = [0] * 1001

# dp 초기화
dp[1] = 1
dp[2] = 3
for i in range(3, n+1):
    # i번째 타일은 i-1번째에서 한 가지, i-2번째에서 두 가지 경우로 파생됌
    dp[i] = (dp[i-1] + 2 * dp[i-2]) % 10007
print(dp[n])