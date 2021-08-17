from itertools import combinations as C
import sys

while True:
    line = list(map(int, sys.stdin.readline().split()))
    # 0을 만나면 종료
    if line[0] == 0: break

    length, number = line[0], line[1:]
    
    # k개의 수 중에서 6개를 조합으로 골라서 출력
    for comb in list(C(number, 6)):
        print(*comb)
    print()

