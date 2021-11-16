import sys, heapq
input = sys.stdin.readline

n = int(input())
lectures = [tuple(map(int, input().split())) for _ in range(n)]
lectures.sort(key = lambda x : -x[0]) # 시작 시간이 빠른 강의부터 뽑기 위해 역순으로 정렬
start, finish = lectures.pop() # 맨 처음 강의를 하나 넣고 시작
endTime = [finish]
answer = 1
while lectures:
    finish = endTime[0]
    s, f = lectures.pop()
    if s < finish: answer += 1
    else: heapq.heappop(endTime)
    # 강의의 끝나는 시간을 항상 우선순위 큐에 삽입
    heapq.heappush(endTime, f)

print(answer)
