
# 가장 마지막 제한 날짜에 강의를 한다고 가정
def check_due(schedule, d):
    cursor = d
    while cursor > 0:
        if schedule[cursor] == True:
            schedule[cursor] = False
            return True
        else:
            cursor -= 1
    return False


if __name__ == "__main__":
    n = int(input())
    if n == 0:
        print(0)
    else:
        # 강연 수익과 제한 날짜를 담는 리스트
        info = []
        for i in range(n):
            p, d = map(int, input().split())
            info.append((p, d))

        # 비용이 큰 순서대로 정렬
        info = sorted(info, key=lambda x: -x[0])
        answer = 0

        # 강연을 할 수 있는 날짜를 체크하는 schedule
        schedule = [True]*10001
        for p, d in info:
            if check_due(schedule, d) == True:
                answer += p
        print(answer)
