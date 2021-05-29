import sys
from collections import defaultdict


def paperCheck(x, y, length):
    start = graph[x][y]
    flag = True
    # 하나라도 종이의 값이 다르면 False 리턴
    for i in range(x, x+length):
        for j in range(y, y+length):
            if graph[i][j] != start:
                flag = False
                break 
        if not flag:
            break
    # 만약 모두 같은 숫자로 이루어진 종이라면
    # paperCount에 해당 숫자의 갯수를 1 증가시킨다.            
    if flag:    
        paperCount[start] += 1

    # 만약 값이 다른 종이가 있다면 length // 3으로 쪼개고
    # 쪼개진 종이에 대해 다시 paperCheck를 재귀적으로 수행
    if not flag:
        for i in range(x, x + length, length//3):
            for j in range(y, y + length, length//3):
                paperCheck(i, j, length//3)


n = int(input())
# 처음 종이 상태 입력받기
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

# -1, 0, 1로 이루어진 종이의 개수를 저장하는 dict
paperCount = defaultdict(int)

# 재귀함수 실행
paperCheck(0,0,n)

# 결과 출력
print(paperCount[-1])
print(paperCount[0])
print(paperCount[1])




