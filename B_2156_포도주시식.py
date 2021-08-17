
# 포도주 잔의 개수
n = int(input())

# 1 ~ n개 잔에 담긴 포도주의 양
wine = [int(input()) for _ in range(n)]
wine.insert(0,0)
if n == 1:
    print(wine[1])
elif n == 2:
    print(wine[1]+wine[2])
elif n == 3:
    print(max(wine[1]+wine[2], wine[2]+wine[3], wine[1]+wine[3]))
else:
    dp = [0] * (n+1)
    dp[1] = wine[1]
    dp[2] = wine[1] + wine[2]
    dp[3] = max(wine[1]+wine[2], wine[2]+wine[3], wine[1]+wine[3])
    # dp[i] = i번째 포도잔까지 최대로 마실 수 있는 포도주의 양
    for i in range(4, n+1):
        # O O X = i-1번째 포도잔을 마셨을 때 최대값
        # O X O = i-2번째 포도잔을 마셨을 때 최대값 + 현재 포도잔 마실 때
        # X O O = i-3번째 포도잔까지 최대로 마신 값 + i-1번째 포도잔을 마시고 현재 포도잔을 마실 때
        dp[i] = max(dp[i-1], dp[i-2] + wine[i], dp[i-3] + wine[i-1] + wine[i])
    print(dp[n])