
if __name__ == "__main__":
    n, k = map(int, input().split())
    coins = [int(input()) for _ in range(n)]
    coins = list(set(coins))     # 가치가 똑같은 동전 제거
    coins.sort()                 # 가치를 내림차순으로 정렬
    answer = []

    dp = [10001 for _ in range(k+1)]
    dp[0] = 0
    for c in coins:             # 가치가 작은 동전부터 dp값 갱신
        for i in range(c,k+1):  
            dp[i] = min(dp[i], dp[i-c] + 1)     # 이전까지 동전으로만 가치 i를 만드는 경우 vs 현재 동전까지 써서 가치 i를 만드는 경우
    answer = dp[k] if dp[k] != 10001 else -1
    print(answer)