import heapq


def find_existing_viruses(graph):
    n = len(graph)
    existing_virus = []
    for i in range(1, n):
        for j in range(1, n):
            if virus[i][j] != 0:
                # 바이러스의 숫자를 튜플 첫번째 원소로 놓아서 최소값 정렬
                heapq.heappush(existing_virus, (virus[i][j], i, j))

    return existing_virus


def spread(virus, existing_virus, s):
    count = 0
    while count < s:  # s초동안 반복
        temp = []
        while existing_virus:
            now = heapq.heappop(existing_virus)
            for i in range(4):
                nx, ny = now[1] + dx[i], now[2] + dy[i]
                if 1 <= nx <= n and 1 <= ny <= n and virus[nx][ny] == 0:
                    virus[nx][ny] = now[0]
                    temp.append((now[0], nx, ny))
        count += 1
        existing_virus.extend(temp)
    return virus


if __name__ == "__main__":
    n, k = map(int, input().split())

    # 초기 바이러스 상태 정보 받기
    virus = [[0] * (n+1) for _ in range(n+1)]
    for i in range(n):
        virus[i+1] = list(map(int, input().split()))
        virus[i+1].insert(0, 0)  # 길이를 n+1로 맞추기

    s, x, y = map(int, input().split())  # s초 후에 x, y에 존재하는 바이러스?
    dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]  # 전파 방향

    existing_virus = find_existing_viruses(virus)
    spread(virus, existing_virus, s)

    print(virus[x][y])
