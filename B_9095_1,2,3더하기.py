

if __name__ == "__main__":
    t = int(input())

    # n = 1, 2, 3 ... 규칙을 찾아보면
    # An = An-1 + An-2 + An-3 (n >= 4)

    # n은 양수이며 11보다 작다는 조건
    dp = [0] * 12
    dp[1], dp[2], dp[3] = 1, 2, 4
    for i in range(4, 12):
        dp[i] = dp[i-1]+dp[i-2]+dp[i-3]

    for _ in range(t):
        n = int(input())
        print(dp[n])
