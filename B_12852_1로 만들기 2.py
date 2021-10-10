n = int(input())

# dp[i] = i를 1로 만드는 데 드는 최소 횟수
dp = [100000] * (n+1)
dp[0] = -1
# dp_route[i] = i에서 1로 갈 때 최단 경로
dp_route = [[] for _ in range(n+1)]

for i in range(1, n+1):
    preIndex = -1;
    dp_route[i].append(i) # 시작점을 경로에 삽입

    # 현재 값 나누기 3, 나누기 2, 빼기 1을 한 값 중 최소 횟수로 1에 도달하는 값을 찾는다.
    if i % 3 == 0 and dp[i // 3] + 1 < dp[i]:
        dp[i] = dp[i // 3] + 1
        preIndex = i // 3
    if i % 2 == 0 and dp[i // 2] + 1 < dp[i]:
        dp[i] = dp[i // 2] + 1
        preIndex = i // 2
    if dp[i-1] + 1 < dp[i]:
        dp[i] = dp[i-1] + 1
        preIndex = i - 1

    # 그 이전 값부터 1까지 가는 경로를 더해준다.
    dp_route[i].extend(dp_route[preIndex])

print(dp[n])
print(*dp_route[n])
