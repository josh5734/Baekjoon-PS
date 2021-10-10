import sys
input = sys.stdin.readline

def findTarget(numbers, target):
    start, end = 0, len(numbers)-1
    while start <= end:
        mid = (start + end) // 2
        if numbers[mid] == target: 
            return mid
        elif numbers[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return -1      

answer = 0
n = int(input())
numbers = list(map(int, input().split()))
numbers.sort() # 오름차순 정렬

for i in range(n):
    for j in range(n):
        # 다른 수 두 개의 합으로 나타내야 함
        target = numbers[i] - numbers[j]
        result = findTarget(numbers, target)
        if result != -1 and i != j and i != result:
            answer += 1
            break
print(answer)