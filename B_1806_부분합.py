import sys
if __name__ == "__main__":
    N, S = map(int, input().split())
    sequence = list(map(int, sys.stdin.readline().split()))

    left, right = 0, 0
    totalSum = 0
    length = 100001
    for left in range(N):  # 왼쪽 포인터를 한칸씩 이동해보면서
        while totalSum < S and right < N:  # 오른쪽 포인터 이동
            totalSum += sequence[right]
            right += 1

        if totalSum >= S:  # 조건을 만족하면
            if right - left < length:
                length = right-left  # 길이 최소값 갱신
        totalSum -= sequence[left]
    # 답 출력
    print(length if length < 100001 else 0)
