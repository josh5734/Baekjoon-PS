import sys
from bisect import bisect_left, bisect_right

if __name__ == "__main__":
    n = int(input())
    house = [int(i) for i in sys.stdin.readline().split()]
    house.sort()

    answer = int(10e12)
    location = 0
    # 왼쪽에서 오른쪽으로 진행하면서 전체 합은 줄어들고 왼쪽부터의 합은 증가
    total_sum, left_sum = sum(house), 0
    for i in range(len(house)):
        left_sum += house[i]
        total_sum -= house[i]
        totalDistance = (i+1) * house[i] - left_sum + \
            total_sum - house[i] * (len(house) - (i+1))
        if totalDistance < answer:  # 가장 작은 값 출력
            answer = totalDistance
            location = i

    print(house[location])
