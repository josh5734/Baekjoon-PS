import heapq as hq

n, m, l = map(int, input().split())
facility = sorted(list(map(int, input().split())))

# 각 휴게소 사이의 거리를 최대힙 구조로 담는다.
# 거리를 큐에 담을 때는 등분한 횟수를 같이 입력하고, 초기값은 1이다.
distance = []
for i in range(len(facility)):
    if i == 0:  # 시작점~첫번째 휴게소 사이 거리
        hq.heappush(distance, (-facility[i],1))
    else:
        hq.heappush(distance, (-(facility[i] - facility[i-1]),1))
    if i == len(facility) - 1: # 마지막 휴게소~끝점 사이 거리
        hq.heappush(distance, (-(l-facility[-1]),1))
    
# 가장 긴 구간을 k등분해나간다.
for _ in range(m):
    if n == 0:
        longest, divided = -l, 1
    else:
        longest, divided = hq.heappop(distance)

    # 등분하기 전 원래 거리값을 k등분으로 해줘야 한다.
    longest = -longest * divided
    hq.heappush(distance, ((-longest / (divided +1)), divided + 1))

answer = -hq.heappop(distance)[0]
if answer == int(answer):
    print(int(answer))
else:
    print(int(answer)+1)