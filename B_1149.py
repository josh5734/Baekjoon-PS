if __name__ == "__main__":
    # 집의 개수
    number_of_house = int(input())

    # 각 집을 R,G,B로 색칠할 때 드는 비용 정보
    rgb_cost = []
    for i in range(number_of_house):
        rgb_cost.append(list(map(int, input().split())))

    # 각 집을 R,G,B로 칠할 때 드는 비용의 합 누적정보
    rgb_cost_total = [[0, 0, 0] for i in range(number_of_house)]

    # 첫번째 집을 R,G,B로 칠할 때 드는 비용 초기화
    rgb_cost_total[0] = rgb_cost[0]

    # 각 집의 R,G,B 누적 최소 비용은 (각 색깔로 해당 집을 칠하는 비용) + (나머지 색깔로 그 전 집까지 칠한 최소 누적 비용)
    for i in range(1, number_of_house):
        rgb_cost_total[i][0] = rgb_cost[i][0] + \
            min(rgb_cost_total[i-1][1], rgb_cost_total[i-1][2])
        rgb_cost_total[i][1] = rgb_cost[i][1] + \
            min(rgb_cost_total[i-1][0], rgb_cost_total[i-1][2])
        rgb_cost_total[i][2] = rgb_cost[i][2] + \
            min(rgb_cost_total[i-1][0], rgb_cost_total[i-1][1])

    # 최소 비용은 rgb_cost_total의 마지막에서 가장 작은 값
    min_cost = min(rgb_cost_total[-1])
    print(min_cost)
