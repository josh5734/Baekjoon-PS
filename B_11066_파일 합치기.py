from collections import deque

def combineChapters(chapters):
    cost = 0
    while len(chapters) > 1:
        a = chapters.popleft()
        b = chapters.popleft()
        cost += (a+b)
        chapters.append(a+b)
        print(chapters)
    print("cost = ", cost)
    return cost

tc = int(input())
for _ in range(tc):
    k = int(input())
    chapters = deque()
    for p in list(map(int, input().split())):
        chapters.append(p)
    cost = 0
    # 챕터의 수가 짝수일 때
    if len(chapters) % 2 == 0:
        cost = combineChapters(chapters)
    else:
        cost = min(chapters[0] + combineChapters(deque(list(chapters)[1:])), combineChapters(deque(list(chapters)[:-1])) + chapters[-1])
    print(cost)
