import sys

if __name__ == "__main__":
    n = int(input())
    # 좌표 정보를 입력받을 리스트 li
    li = []

    for i in range(n):
        # N의 크기가 100,000까지 갈 수 있으므로 stdin으로 입력받기
        li.append(tuple(map(int, sys.stdin.readline().split())))
    # li를 x좌표, y좌표의 오름차순 순서로 정렬
    li.sort(key = lambda x: (x[0], x[1]))

    for loc in li:
        print(loc[0], loc[1])
