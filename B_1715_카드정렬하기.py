import sys
import heapq

if __name__ == "__main__":
    answer = 0
    n = int(input())
    cards = []
    for _ in range(n):
        heapq.heappush(cards, int(sys.stdin.readline().rstrip()))

    while len(cards) > 2:  # (a+b)+(a+b+c) VS (a+b)+(c+d) --> a+b vs d
        root = heapq.heappop(cards)
        c = heapq.heappop(cards)
        heapq.heappush(cards, root + c)
        answer += (root + c)

    answer += sum(cards)
    print(answer)
