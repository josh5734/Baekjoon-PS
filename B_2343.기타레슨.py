import sys


def b_search(start, end):
    while start <= end:
        # 사용할 수 있는 블루레이의 개수 초기화(맨 처음 하나 제외)
        blueray = m-1
        mid = (start + end) // 2
        time_sum = 0
        for t in times:
            if (time_sum + t) <= mid:
                time_sum += t
            # 새로운 블루레이 사용
            else:
                time_sum = t
                blueray -= 1

        if blueray >= 0:
            answer = mid
            end = mid - 1
        elif blueray < 0:
            start = mid + 1
    return answer


if __name__ == "__main__":
    # 레슨의 수, 블루레이의 수
    n, m = map(int, input().split())
    # 레슨 순서대로 기타 레슨의 길이
    times = list(map(int, sys.stdin.readline().split()))

    # 최소는 제일 긴 레슨의 시간, 최대는 모든 레슨이 하나의 블루레이에 들어갈때라고 가정 -> 10억
    start, end = max(times), int(1e9)
    answer = 0

    answer = b_search(start, end)
    print(answer)
