import sys
sys.setrecursionlimit(100000)

def makeTeam(curr):
    dest = graph[curr]
    if startMemo == dest:
        return 1
    elif curr == dest:
        return -1
    else:
        return makeTeam(dest)    


tc = int(input())
for _ in range(tc):
    n = int(input())
    answer = n

    graph = list(map(int, sys.stdin.readline().split()))
    graph.insert(0,0) # 학생 번호 맞춰주기

    for curr in range(1,n+1):
        if curr == graph[curr]:
            answer -= 1
        else:
            startMemo = curr
            if makeTeam(curr) == 1:
                answer -= 1
    print(answer)    