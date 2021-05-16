import sys

def binary_search(target):
    left, right = 0, len(my_cards)-1
    answer = 0
    while left <= right:
        mid = (left + right) // 2
        if my_cards[mid] >= target:
            right = mid - 1
            answer = mid
        else:
            left = mid + 1
    return my_cards[answer] == target


answer = []
n = int(input())
# 내가 가지고 있는 카드를 정렬
my_cards = list(map(int, sys.stdin.readline().split()))
my_cards.sort()

# 가지고 있는지를 확인해야 하는 카드
m = int(input())
given = list(map(int, sys.stdin.readline().split()))
for c in given:
    # 이분 탐색으로 현재 수가 존재하는지 확인
    if binary_search(c):
        answer.append("1")
    else:
        answer.append("0")

print(' '.join(answer))