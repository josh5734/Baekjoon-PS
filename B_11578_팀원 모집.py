from itertools import combinations as C
n, m = map(int, input().split())

prob = []
# 각 친구가 풀 수 있는 문제를 비트화해서 저장한다.
for i in range(m):
    temp = 0b00000000000
    for p in list(map(int, input().split()))[1:]:
        temp |= (1 << p)
    prob.append(temp)

answer = -1
# k명의 친구를 선택해서 모든 문제를 풀 수 있는지 확인한다.
for k in range(m+1):
    solved = list(C(prob, k))
    stop = False
    for solve in solved:
        temp = 0b0000000000
        for s in solve:
            temp |= s
        # 모든 문제를 풀 수 있으면 종료 
        if temp == 2 ** (n+1) - 2:
            answer = k
            stop = True
            break
    if stop:
        break            
print(answer)