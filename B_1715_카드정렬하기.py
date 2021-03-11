import sys
import heapq

if __name__ == "__main__":
    answer = 0
    n = int(input())
    cards = []
    for _ in range(n):
        heapq.heappush(cards, int(sys.stdin.readline().rstrip()))

    if len(cards) == 1:  # 카드 묶음이 하나면 섞을 필요 X
        answer = 0
    elif len(cards) == 2:  # 카드 묶음이 두 개면 그냥 두개를 합치면 됌
        answer += sum(cards)

    else:
        while len(cards) > 2:  # (a+b)+(a+b+c) VS (a+b)+(c+d) --> a+b vs d
            root = heapq.heappop(cards)
            c = heapq.heappop(cards)
            d = heapq.heappop(cards)
            if root + c >= c + d:
                heapq.heappush(cards, root)
                heapq.heappush(cards, c+d)
                answer += (c+d)
            else:
                heapq.heappush(cards, d)
                heapq.heappush(cards, root + c)
                answer += (root + c)
        answer += sum(cards)
    print(answer)
