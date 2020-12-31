from collections import Counter
import sys


if __name__ == "__main__":
    n = int(input())

    dic = dict()
    line = list(map(int, sys.stdin.readline().split()))

    coor = sorted(Counter(line).items(), reverse=True)

    count = 1
    for c in coor:
        dic[c[0]] = len(coor) - count
        count += 1

    for num in line:
        print(dic[num], end=' ')
