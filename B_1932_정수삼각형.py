import sys
if __name__ == "__main__":
    size = int(input())

    # 삼각형 만들기
    triangle = [[]]
    for _ in range(size):
        triangle.append(list(map(int, sys.stdin.readline().split())))

    # dp를 이용하기 위해 층마다 최대값을 저장할 테이블 생성
    dp = [[] for _ in range(size+1)]

    dp[1].append(triangle[1][0])

    # 한 칸씩 내려가면서 그 위 칸값들과 현재 칸의 값들을 대각선으로 더해서 후보를 쌓아나간다.
    for i in range(2, size+1):
        for j in range(i):
            if j == 0:
                dp[i].append(triangle[i][j] + dp[i-1][0])
            elif j == i-1:
                dp[i].append(triangle[i][j] + dp[i-1][j-1])
            else:
                dp[i].append(max(triangle[i][j] + dp[i-1][j-1],
                                 triangle[i][j] + dp[i-1][j]))

    print(max(dp[-1]))
