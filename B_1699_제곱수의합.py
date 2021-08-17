## pypy3 ##
n = int(input())

dp = [0] * (n+1)
dp[1] = 1

for  i in range(2, n+1):
    # i보다 작은 제곱수들의 집합을 구하기
    pieces = [x ** 2 for x in range(1, int((i**0.5))+1)]

    # dp[i] = 자기 자신보다 작은 제곱수로 쪼개는 횟수(=1) + 제곱수를 최소개수로 표현하는 값(=dp[i-p])
    minCount = 1000000
    for p in pieces:
        count = 1 + dp[i -p]
        if minCount > count:
            minCount = count
    dp[i] = minCount
print(dp[n])