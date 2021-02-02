import sys

if __name__ == "__main__":
    trees = {}
    total = 0
    # 입력받기
    while True:
        tree = sys.stdin.readline().rstrip()
        if tree:
            total += 1
            if trees.get(tree):
                trees[tree] += 1
            else:
                trees[tree] = 1
        else:
            break

    # 나무들을 사전순으로 정렬
    trees = sorted(trees.items())

    for t in trees:
        # 소수점 넷째짜리까지 표현
        percent = round(100*t[1]/total, 4)
        print(t[0], '%.4f' % percent)
