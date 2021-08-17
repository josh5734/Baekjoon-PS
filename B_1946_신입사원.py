n = int(input())

cnt = 0
while(cnt < n):
    candidates = int(input())
    score = []

    for i in range(candidates):
        score.append(tuple(map(int, input().split(" "))))

    score = sorted(score, key=lambda paper: paper[0])

    best = score[0][1]
    for i in range(candidates):
        if score[i][1] > best:
            candidates -= 1
        else:
            best = score[i][1]
    cnt += 1

    print(candidates)
