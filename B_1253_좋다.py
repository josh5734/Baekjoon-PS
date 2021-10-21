import sys
from bisect import bisect_left, bisect_right
input = sys.stdin.readline

def findTargetRange(numbers, target, i, j):
    left = bisect_left(numbers, target)
    right = bisect_right(numbers, target)
    return [idx for idx in range(left, right) if idx != i and idx != j]
    
answer = 0
n = int(input())
numbers = list(map(int, input().split()))
numbers.sort() # 오름차순 정렬

for i in range(n):
    for j in range(n):
        # 다른 두 수의 합으로 나타낸다 -> i, j는 달라야함
        if i == j: continue
        target = numbers[i] - numbers[j]
        # 주어진 배열에서 i, j를 제외하고 target값이 존재하는지 확인
        result = findTargetRange(numbers, target, i, j)
        if len(result) >= 1:
            answer += 1
            break
print(answer)