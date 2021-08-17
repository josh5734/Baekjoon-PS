if __name__ == "__main__":
    # 계단의 개수
    steps = int(input())
    # 각 계단의 점수 // 첫번째 계단 포함
    scores = [0]
    for i in range(steps):
        scores.append(int(input()))

    # 각 계단에서 최대 점수를 계산하는 리스트
    # 해당 계단을 밟을 때 건너뛰어서 밟는지, 연속해서 밟는지에 따라 경우를 나눠서 계산
    score_list = [[0, 0] for i in range(steps+1)]
    score_list[0] = [0, 0]
    score_list[1] = (scores[1], 0)

    for i in range(2, steps+1):
        score_list[i][0] = scores[i] + max(score_list[i-2])
        score_list[i][1] = scores[i] + score_list[i-1][0]

    # 마지막 계단에서 최대값
    print(max(score_list[-1]))
