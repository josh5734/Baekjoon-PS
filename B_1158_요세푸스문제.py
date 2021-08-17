

if __name__ == "__main__":

    answer = []
    n, k = map(int, input().split())

    # N명의 사람 입력 받기
    circle = [i for i in range(1, n+1)]

    # 현재 위치를 나타내는 커서
    cursor = -1
    while True:
        count = 0
        while True:
            cursor += 1
            # 커서가 원순열의 끝에 오면 다시 원점으로 이동
            if cursor == n:
                cursor = 0
            if circle[cursor] != -1:
                count += 1
                if count == k:
                    answer.append(str(circle[cursor]))
                    circle[cursor] = -1
                    break

        # 모든 사람이 다 제거된 시점
        if len(answer) == n:
            break
    answer = ', '.join(answer)
    print(f'<{answer}>')
