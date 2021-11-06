import sys
input = sys.stdin.readline

n = int(input())
number = [0] + list(map(int, input().split()))

# dp[i][j] = i~j번째 수를 선택했을 때 팰린드롬인가?
dp = [[False] * (n+1) for _ in range(n+1)]

# 자기 자신은 항상 팰린드롬
for i in range(1, n+1): dp[i][i] = True

# 연속된 두 수가 팰린드롬이려면 서로 같아야 함
for i in range(1, n):
    if number[i] == number[i+1]:
        dp[i][i+1] = True
    
# dp[i][j]를 결정하기 위해서는 dp[i-1][j+1]을 알아야한다.
# Memoization의 순서를 i는 내림차순, j는 오름차순으로 실행
for i in range(n-1, 0, -1):
    for j in range(i+1, n+1):
        if(dp[i+1][j-1] and number[i] == number[j]):
            dp[i][j] = True

for i in range(int(input())):
    s, e = map(int, input().split())
    isPalindrome = 1 if dp[s][e] else 0
    print(isPalindrome)

