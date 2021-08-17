

#########################################################3

n, k = map(int, input().split())

coins = [int(input()) for _ in range(n)]
coins = list(set(coins))    # 중복 동전 제거
coins.sort()    # 오름차순 정렬
n = len(coins)

# dp[i] = i번째 동전까지 써서 k원을 만드는 경우의 수
# 다른 풀이 참고
dp = [0 for _ in range(k+1)]
dp[0] = 1 
for c in coins:
    for j in range(c, k+1):
        dp[j] += dp[j-c]
print(dp[k])


'''
# 시간, 메모리 제한??????
# 원래 풀이
n, k = map(int, input().split())
dp = [[0] * (k+1) for _ in range(n+1)]

# dp[i][j] = 동전을 오름차순 정렬한 상태에서 
# i번째 동전까지 사용할 수 있을 때 j원을 만들 수 있는 경우의 수

coins = [int(input()) for _ in range(n)]
coins = list(set(coins))
coins.sort()

for i in range(1,k+1):
    dp[1][i] = 1 if i % coins[0] == 0 else 0

for i in range(2, n+1):
    value = coins[i-1]
    for j in range(1, k+1):
        for t in range(j//value+1):
            if j - (value*t) == 0: dp[i][j] += 1
            else: dp[i][j] += dp[i-1][j - (value * t)]
print(dp[n][k])
'''

