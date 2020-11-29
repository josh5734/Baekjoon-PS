import sys

if __name__ == "__main__":
    # 입력받을 정수의 개수
    n = int(input())

    # 정수 입력받기
    numbers = list(map(int, sys.stdin.readline().rstrip().split()))

    # 각 숫자를 선택했을 때 현재까지 최대값을 담는 리스트
    total_sum = [0] * n
    total_sum[0] = numbers[0]

    # 이전까지 숫자를 안 더하고, 자기 자신에서 새로 시작하는 경우
    # 이전까지 숫자 합에서 큰 부분 + 자기 자신까지 이어서 더하는 경우
    for i in range(1, n):
        total_sum[i] = max(numbers[i], numbers[i] + total_sum[i-1])

    # 최대값 출력
    print(max(total_sum))
