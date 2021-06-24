

if __name__ == "__main__":
    n, k = map(int, input().split())

    bag = [[0, 0]]
    for _ in range(n):
        bag.append(list(map(int, input().split())))

    # 가방에 담고 있는 물건 가치의 dp table
    dp = [[0 for _ in range(k+1)] for _ in range(n+1)]

    max_value = 0
    # 각 i번째 물건까지 담을 수 있다고 생각했을 때
    for i in range(1, n+1):
        # 각 무게까지 담을 수 있는 최대 value
        for j in range(1, k+1):
            if bag[i][0] > j:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = max(bag[i][1] + dp[i-1]
                               [j-bag[i][0]], dp[i-1][j])

    print(dp[n][k])