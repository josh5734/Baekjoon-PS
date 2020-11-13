import sys
from bisect import bisect_left, bisect_right


if __name__ == "__main__":
    # 숫자 정보 입력받기
    n = int(input())
    arr = sorted(sys.stdin.readline().rstrip().split())

    # 탐색 숫자 정보 입력받기
    m = int(input())
    numbers = sys.stdin.readline().rstrip().split()

    # numbers에 대하여 각 숫자가 arr에 몇 개 존재하는지 확인
    for num in numbers:
        # 해당 숫자가 arr에 없으면 같은 곳에 start, end가 생김 -> result = 0
        # 해당 숫자가 arr에 있으면 왼쪽에 start, 오른쪽에 end가 생김 -> result = end - start
        start, end = (bisect_left(arr, num), bisect_right(arr, num))
        result = end - start
        print(result, end=" ")
