import sys

# 이진 탐색 실행


def b_search(arr, target, start, end):

    if start > end:
        return False
    mid = (start + end) // 2

    if(arr[mid] == target):
        return True
    elif(arr[mid] > target):
        return b_search(arr, target, start, mid-1)
    else:
        return b_search(arr, target, mid+1, end)


if __name__ == "__main__":
    # 숫자 정보 입력받기
    n = int(input())
    arr = sorted(sys.stdin.readline().rstrip().split())

    # 탐색 숫자 정보 입력받기
    m = int(input())
    numbers = sys.stdin.readline().rstrip().split()

    # numbers에 대하여 각 숫자가 arr에 존재하는 지 확인
    for num in numbers:
        result = 1 if b_search(arr, num, 0, n-1) == True else 0
        print(result)
