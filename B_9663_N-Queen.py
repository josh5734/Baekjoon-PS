def backTracking(rowPos):
    global answer  
    
    # 퀸을 모두 배치했다면 끝
    if rowPos == n:
        answer += 1
        return
    
    for col in range(n):
        flag = True
        for row in range(rowPos):
            if queenLocation[row] == col or rowPos - row == abs(col - queenLocation[row]):
                flag = False
                break
        if flag:
            queenLocation[rowPos] = col
            backTracking(rowPos + 1)
    
n = int(input())
answer = 0
# 각 row마다 queen이 위치하는 인덱스를 저장하는 리스트
queenLocation = [0] * n
backTracking(0)
print(answer)
