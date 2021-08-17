import sys, heapq
n = int(input())    # 연산의 개수
pq = []          # 절댓값을 담는 우선순위 큐

# 연산의 개수만큼 연산 수행
for _ in range(n):
    x = int(sys.stdin.readline().rstrip())
    
    # x가 0이면 절댓값이 가장 작은 값, 같은 값이 여러개면 가장 작은 수 출력
    if x == 0:
        if len(pq) == 0:
            print(0)
        else:
            print(heapq.heappop(pq)[1])

    # x != 0 이면 절댓값 힙에 값 추가
    # 우선순위 큐는 Comparator가 튜플을 iterate하면서 우선순위 결정해줌
    else:
        if x < 0:
            heapq.heappush(pq, (-x, x))
        else:
            heapq.heappush(pq, (x,x))
