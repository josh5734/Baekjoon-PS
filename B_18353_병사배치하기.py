import sys
if __name__ == "__main__":
    n = int(input())
    answer = 0
    soldier = list(map(int, sys.stdin.readline().split()))
    # 그 이전까지 자신보다 큰 값에 대해 가장 긴 감소하는 수열의 길이 + 1
    decreasing = [1] * n
    for i in range(1, n):
        longest = 0
        for j in range(0, i):
            if soldier[j] > soldier[i]:
                if decreasing[j] > longest:
                    longest = decreasing[j]
        decreasing[i] += longest

    print(n - max(decreasing))
