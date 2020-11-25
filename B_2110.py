import sys

if __name__ == "__main__":

    # 숫자 정보 입력받기
    n, c = map(int, input().split())
    # 집 위치 정보 기록
    arr = []
    for i in range(n):
        arr.append(int(input()))
    arr.sort()

    start, end = arr[0], arr[-1]
    result = 0

    while(start <= end):
        total = 0
        mid = (start + end) // 2
        for house in arr:
            if house % mid == 0:
                total += 1
        if total < c:
            end = mid - 1
        else:
            result = mid
            start = mid + 1

    print(result)
