n = int(input())
cardPack = list(map(int,input().split()))
cardPack.insert(0,0)    # 카드팩의 번호를 1부터 시작

dp = [0] * (n+1)
dp[1] = cardPack[1]
# dp[i] = 카드를 총 i장까지 샀을 때 최대로 지불할 수 있는 금액으로 정의하면
# j번째 카드팩을 산다면 총 i-j 장까지 카드를 샀을 때 최대금액과 비교하면 된다.
for i in range(2, n+1):
    maxValue = 0
    for j in range(i):
        if maxValue <= cardPack[i-j] + dp[j]:
            maxValue = cardPack[i-j] + dp[j]
    dp[i] = maxValue
print(dp[n])