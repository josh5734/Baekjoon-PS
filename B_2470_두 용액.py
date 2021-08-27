import sys
input = sys.stdin.readline

answer = []
n = int(input())
liquid = list(map(int, input().split()))
liquid.sort()
# 산성 용액으로만 이루어진 경우
if liquid[0] > 0:
    answer.extend(liquid[:2])

# 알칼리 용액으로만 이루어진 경우
elif liquid[-1] < 0:
    answer.extend(liquid[-2:])


# 산성, 알칼리 용액이 둘 다 있는 경우
# 주의) 이 경우에도 산성, 알칼리 용액만으로 최소값을 만들 수 있다.
else:
    # 투 포인터 이용
    left, right = 0, len(liquid) - 1
    min_diff = 2000000001
    while left < right:
        diff = liquid[left] + liquid[right]

        if abs(diff) < min_diff:
            answer = [liquid[left], liquid[right]]
            min_diff = abs(diff)

        if diff > 0:
            right -= 1
        
        elif diff < 0:
            left += 1
        
        else:
            break
print(*answer)



# 이분탐색 이용한 풀이
'''
from bisect import bisect_left
input = sys.stdin.readline


# target과 가장 가까운 숫자의 인덱스를 리턴
def findClosestIndex(plus, target):
    idx = bisect_left(plus, target)
    if idx == len(plus):
        return idx - 1
    elif plus[idx] == target:
        return idx
    elif idx > 0:
        j = idx -1
        if plus[idx] - target > target - plus[j]:
            return j
    return idx

answer = []
n = int(input())
plus, minus = [], []
for l in list(map(int, input().split())):
    plus.append(l) if l > 0 else minus.append(l)
plus.sort()
minus.sort(reverse=True)

# 산성 용액으로만 이루어진 경우
if len(plus) == 0:
    answer = minus[:2][::-1]

# 알칼리 용액으로만 이루어진 경우
elif len(minus) == 0:
    answer = plus[:2]

# 산성, 알칼리 용액이 둘 다 있는 경우
# 주의) 이 경우에도 산성, 알칼리 용액만으로 최소값을 만들 수 있다.
else:   
    minSum = 2000000001
    if len(minus) > 1:
        tempSum = abs(sum(minus[:2]))
        if tempSum < minSum:
            minSum = tempSum
            answer = minus[:2][::-1]

    if len(plus) > 1:
        tempSum = sum(plus[:2])
        if tempSum < minSum:
            minSum = tempSum
            answer = plus[:2]

    for m in minus:
        closestIndex = findClosestIndex(plus, -m)
        tempSum = abs(m + plus[closestIndex])
        if tempSum < minSum:
            minSum = tempSum
            answer = [m, plus[closestIndex]]
print(*answer)
'''