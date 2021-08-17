if __name__ == "__main__":
    case = int(input())

    # n, m input받기
    for i in range(case):
        n, m = map(int, input().split())
        multiplier, divider, cnt = 1, 1, 0

        # 조합
        while(cnt < n):
            multiplier *= (m - cnt)
            divider *= (n - cnt)
            cnt += 1
        answer = multiplier // divider

        print(answer)
