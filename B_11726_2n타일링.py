

if __name__ == "__main__":
    n = int(input())

    # n의 범위는 1부터 1000까지
    dp = [0] * (n+1)

    # 크기가 2*1짜리 타일, 2*2짜리 타일 2개로 모든 타일의 조합을 생성 가능
    # 1과 2의 조합으로 계산 --> 규칙찾기
    # An = An-1 + An-2(n>=2)
    if n == 1:
        print(1)
    else:
        dp[1], dp[2] = 1, 2
        for i in range(3, n+1):
            dp[i] = (dp[i-1] + dp[i-2]) % 10007

        print(dp[n])
