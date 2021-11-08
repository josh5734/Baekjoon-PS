import sys
input = sys.stdin.readline

n = int(input())
sequence = list(map(int, input().split()))
dp = [0] * n
answer = 0
for i in range(n):
    maxPrev, prevIdx = 0, 0
    for j in range(i):
        if sequence[j] < sequence[i]:
            if maxPrev < dp[j]:
                maxPrev = dp[j]
                prevIdx = j
    dp[i] = dp[prevIdx] + 1
    if dp[i] > answer:
        answer = dp[i]
print(answer)
    