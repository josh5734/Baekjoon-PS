if __name__ == "__main__":
    start = int(input())
    optimal_time_list = [0]*1000001

    # 1에서 시작해서 1이 되는 경우는 0 // 2에서 1이 되기 위해서는 1번, 3에서 1이 되기 위해서는 1번 <- 초기화
    optimal_time_list[1] = 0
    optimal_time_list[2] = 1
    optimal_time_list[3] = 1

    for i in range(4, start+1):
        # 현재 수에서 1을 빼는 경우
        optimal_time_list[i] = optimal_time_list[i-1] + 1

        # 현재 수가 2로 나누어 떨어지는 경우
        # 1을 빼는 경우와 2로 나누는 경우 중에서 더 작은 쪽
        if i % 2 == 0:
            optimal_time_list[i] = min(
                optimal_time_list[i], optimal_time_list[i // 2] + 1)

        # 현재 수가 3로 나누어 떨어지는 경우
        # 1을 빼는 경우와 2로 나누는 경우, 3으로 나누는 경우 중에서 더 작은 쪽
        if i % 3 == 0:
            optimal_time_list[i] = min(
                optimal_time_list[i], optimal_time_list[i // 3] + 1)

    print(optimal_time_list[start])
