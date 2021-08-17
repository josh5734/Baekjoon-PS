
def available(x):
    for i in range(1, x):
        if row[x] == row[i] or abs(row[x]-row[i]) == x - i:
            return False
    return True


def nqueen(cnt):


if __name__ == "__main__":
    # 체스판 크기
    n = int(input())
    answer = 0

    # 각 행을 나타내는 배열 row
    row = [0 for _ in range(16)]

    nqueen(1)
