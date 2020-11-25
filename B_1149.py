if __name__ == "__main__":
    house = int(input())
    cost = []
    for i in range(house):
        cost.append(list(map(int, input().split())))

    dp = [0] * 1000
    dp[0] = min(cost[0])
    flag = cost[0].index(dp[0])

    for h in range(1, house):
        temp = []
        for c in range(3):
            if c != flag:
                temp.append(cost[h][c])
        dp[h] = min(temp)
        flag = cost[h].index(dp[h])

    print(dp)
