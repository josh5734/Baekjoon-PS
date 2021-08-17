

n = int(input())

# n <= 2일 때
if n == 1:
    print(10)
elif n == 2:
    print(55)

# n >= 3 일 때
else:
    # dp[i][j] = i-1 번째에서 맨 끝자리 숫자가 9 - j일 때 만들 수 있는 오르막 수
    dp = [[0] * 10 for _ in range(n+1)]
    dp[1] = [1,1,1,1,1,1,1,1,1,1]
    dp[2] = [10,9,8,7,6,5,4,3,2,1]
    
    for i in range(3, n+1):
        start = sum(dp[i-1])
        dp[i][0] = start
        for j in range(1, 10):
            start -= dp[i-1][j-1]
            dp[i][j] += start 
    print(sum(dp[n]) % 10007)
    
