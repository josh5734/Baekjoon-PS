import sys
from collections import deque


def do_homework(doing, works):
    # 시작 시간 초기화
    time, score = 1, 0
    # 처음 과제를 스택에 넣고 시작
    work = works.popleft()
    doing.append(work)
    while(time <= n):
        # 현재 과제를 하고 있는 상태
        if len(doing) > 0:
            time += 1
            doing[-1][2] -= 1
            # 과제가 끝나면 점수를 더하고 pop
            if doing[-1][2] == 0:
                score += doing[-1][1]
                doing.pop()
                if len(works) > 0:
                    time = works[0][0]
                    doing.append(works.popleft())
                elif len(works) == 0 and len(doing) == 0:
                    return score
            if len(works) != 0 and time == works[0][0]:
                doing.append(works.popleft())

        #print("time:", time, "stack:", doing)
    return score


if __name__ == "__main__":
    # 과제하는 데 주어진 총 시간
    n = int(input())

    # 주어진 과제들의 정보 입력받기
    works = deque()
    for t in range(1, n+1):
        line = sys.stdin.readline().split()
        if line[0] != '0':
            grade, time = int(line[1]), int(line[2])
            works.append([t, grade, time])

    doing = []
    score = 0 if len(works) == 0 else do_homework(doing, works)
    print(score)
