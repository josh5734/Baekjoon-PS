import sys
if __name__ == "__main__":
    answer = 0
    n, c = map(int, input().split())
    house = []
    for _ in range(n):
        house.append(int(sys.stdin.readline().rstrip()))
    house.sort()  # 원점을 기준으로 정렬

    start, end = 0, int(1e10)
    while start <= end:
        cursor = house[0]  # 첫번째 집을 기준
        mid = (start + end) // 2
        count = 1
        # 현재로부터 mid 만큼 떨어진 곳보다 멀리 집이 있다면 거기에 공유기 설치를 해본다.
        for i in range(1, len(house)):
            if house[i] >= cursor + mid:
                count += 1
                cursor = house[i]

        if count >= c:  # 모든 집을 돌아본 뒤 공유기가 C보다 많이 설치 되었다면 공유기 사이의 거리를 더 늘려서 가능한 집을 줄여보자.
            start = mid + 1
            answer = mid
        else:
            end = mid - 1
    print(answer)
