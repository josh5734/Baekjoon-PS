import sys

if __name__ == "__main__":
    # 회의의 수
    n = int(input())

    meetings = []
    for _ in range(n):
        meetings.append(tuple(map(int, sys.stdin.readline().split())))

    # 각 회의를 일찍 시작하는 순서대로 정렬
    meetings.sort()
    # 사용할 회의를 담을 리스트
    use = [meetings[0]]

    for i in range(1, n):
        # 각 회의의 시작, 종료 시간
        start, end = meetings[i][0], meetings[i][1]
        if use[-1][0] <= start < use[-1][1] and end <= use[-1][1]:
            use.pop()
            use.append(meetings[i])
        elif start >= use[-1][1]:
            use.append(meetings[i])

    # 사용하는 회의 수 출력
    print(len(use))
