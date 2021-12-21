from bisect import bisect_left, bisect_right

def getParitalSumArray(array):
    result = []
    length = len(array)
    for i in range(length):
        for j in range(i, length):
            temp = sum(array[i:j+1])
            result.append(temp)
    return sorted(result)

def binarySearch(array, target):
    # target이 위치할 수 있는 왼쪽과 오른쪽 인덱스를 구한다.
    left_index = bisect_left(array, target)
    right_index = bisect_right(array, target)
    count = right_index - left_index
    return count

t = int(input())
n = int(input())
array_A = list(map(int, input().split()))
m = int(input())
array_B = list(map(int, input().split()))

answer = 0
sumOfArray_A = getParitalSumArray(array_A)
sumOfArray_B = getParitalSumArray(array_B)

for x in sumOfArray_A:
    # 전체 합에서 A배열의 합을 뺀 값이 B배열에 몇 개 존재하는가?
    rem = t - x
    answer += binarySearch(sumOfArray_B, rem)

print(answer)