import sys


if __name__ == "__main__":
    n = int(input())
    time, pay = [0], [0]
    for i in range(n):
        t, p = map(int, sys.stdin.readline().split())
        time.append(t)
        pay.append(p)
    max_benefit = [0 for _ in range(n+1)]

    # 동적 계획법은 전체 문제를 작은 문제로 단순화한 다음 점화식으로 만들어 재귀적인 구조를 활용해서 전체 문제를 해결
    # Memoization - 어떻게 앞의 정보를 활용할 것인가?

    for day in range(1, n+1):
        if day + time[day] <= (n+1):
            # 현재 일해서 벌 수 있는 돈으로 dp 테이블 초기화를 하고 그 이전까지 날 들 중에서 일을 해도 현재에 지장없는 경우 중 최대값으로 초기화
            max_benefit[day] = pay[day]
            for past in range(day):
                if past + time[past] <= day and max_benefit[day] <= max_benefit[past] + pay[day]:
                    max_benefit[day] = max_benefit[past] + pay[day]
    print(max(max_benefit))
