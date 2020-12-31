import sys


if __name__ == "__main__":
    n = int(input())

    # 수열 정보
    sequence = list(map(int, sys.stdin.readline().split()))

    # 현재 숫자까지 가장 긴 증가하는 부분 수열의 길이는 1이거나 그 전 자신보다 작은 값의 가장 긴 증가하는 부분 수열 길이 + 1
    dp = [1] * n
    for i in range(1, n):
        temp = 0
        for j in range(0, i):
            if sequence[i] > sequence[j]:
                if dp[j] > temp:
                    temp = dp[j]

        dp[i] += temp

    print(max(dp))
