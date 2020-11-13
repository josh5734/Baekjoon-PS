import sys

if __name__ == "__main__":

    # 숫자 정보 입력받기
    k, n = map(int, input().split())
    # 랜선 길이 정보 입력받기
    arr = []
    for i in range(k):
        arr.append(int(input()))
    start = 1
    end = max(arr)
    # 이진 탐색 수행
    result = 0
    while(start <= end):
        total = 0
        mid = (start + end) // 2
        #print("mid: ", mid)
        for x in arr:
            # 각 x에 대해 몇개로 잘릴 수 있는지 total에 합산
            if x >= mid:
                total += x // mid
        # print(total)
        if total < n:
            end = mid - 1
        else:
            result = mid
            start = mid + 1

    print(result)
