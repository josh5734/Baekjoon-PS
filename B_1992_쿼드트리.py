import sys


def checkCompress(x,y,length, corner):
    global answer
    start = video[x][y]

    canCompress = True    
    for i in range(x, x+length):
        for j in range(y, y+length):
            if video[i][j] != start:
                canCompress = False
                break
    
    if canCompress:
        answer += start
        #if corner == 3:
        #    answer += ')'
        return True

    else:
        answer += "("
        for i in range(4):
            checkCompress(x + d[i][0] * (length // 2), y+d[i][1] * (length // 2), length // 2, i)
        answer += ')'

n = int(input())
video = []
for _ in range(n):
    video.append(sys.stdin.readline().rstrip())

d = [[0,0],[0,1],[1,0],[1,1]]

answer = ""

checkCompress(0,0,n,0)


print(answer)