from collections import Counter

import sys


if __name__ == "__main__":
    n, m = map(int, input().split())

    people = []
    answer = []

    for _ in range(n):
        people.append(sys.stdin.readline().rstrip())
    for _ in range(m):
        people.append(sys.stdin.readline().rstrip())

    # 이름을 사전순으로 정렬
    c = sorted(Counter(people).items())
    for p in c:
        if p[1] == 2:
            answer.append(p[0])

    # 출력
    print(len(answer))
    for p in answer:
        print(p)
