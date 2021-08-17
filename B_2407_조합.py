
n, m = map(int, input().split())

# n>=5, m>=5
# 파스칼의 삼각형 nCr = n-1Cr-1 + n-1Cr

dp = [[1] * i for i in range(1, 102)]
for i in range(2, 101):
    for j in range(1, i):
        dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
print(dp[n][m])



# 재귀 -> 시간 초과 
'''
def combination(n, m):
    if n == 0 or m == 0 or n == m:
        return 1
    else:
        return combination(n-1, m-1) + combination(n-1, m)    

n, m = map(int, input().split())

# nCr = n-1 C r-1 + n-1 C r재귀 이용
answer = 0
answer += combination(n, m)
print(answer)
'''