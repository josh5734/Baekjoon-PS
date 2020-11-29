import sys

if __name__ == "__main__":

    # 숫자 정보 입력받기
    n, m = map(int, input().split())
    # 랜선 길이 정보 입력받기
    arr = list(map(int, sys.stdin.readline().rstrip().split(" ")))
    start = 0
    end = max(arr)
    # 이진 탐색 수행
    result = 0
    while(start <= end):
        total = 0
        mid = (start + end) // 2
        for x in arr:
            # 각 x에 대해 자르고 남은 부분 계산
            if x > mid:
                total += (x-mid)
        if total < m:
            end = mid - 1
        else:
            result = mid
            start = mid + 1
    print(result)
