import sys


if __name__ == "__main__":
    t = int(input())

    for _ in range(t):
        n = int(input())

        # 각 행의 스티커 위치마다 점수의 최대값을 담는 dp
        dp1 = [0 for _ in range(n)]
        dp2 = [0 for _ in range(n)]

        sticker = []
        for _ in range(2):
            sticker.append(list(map(int, sys.stdin.readline().split())))

        # dp 초기화
        dp1[0] = sticker[0][0]
        dp2[0] = sticker[1][0]

        dp1[1] = sticker[1][0]+sticker[0][1]
        dp2[1] = sticker[0][0]+sticker[1][1]

        # 각 스티커의 최대는 그 바로 이전 스티커 지그재그 + 현재 스티커의 값 혹은 그 이전의 이전 스티커 중 최대값과 현재 스티커값의 합 중에 최대
        for i in range(2, n):
            dp1[i] = max(dp2[i-1]+sticker[0][i],
                         max(dp1[i-2], dp2[i-2]) + sticker[0][i])
            dp2[i] = max(dp1[i-1]+sticker[1][i],
                         max(dp1[i-2], dp2[i-2]) + sticker[1][i])

        print(max(max(dp1), max(dp2)))
