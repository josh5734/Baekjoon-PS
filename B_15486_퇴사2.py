import sys

# 다시보기 #
if __name__ == "__main__":
    # 남은 날 수
    day = int(input())

    # 급여
    total = 0

    # 상담 소요 시간, 급여
    time_and_payment = []
    for i in range(day):
        time_and_payment.append(list(map(int, sys.stdin.readline().split())))
        # 끝나는 날짜 정보 추가
        time_and_payment[i].append(i+time_and_payment[i][0])

        # 상담 불가능한 고객은 0원 처리
        if (i + time_and_payment[i][0] > day):
            time_and_payment[i][1] = 0

    # 현재 날짜에서 일하면 버는 최대 수익을 보여주는 리스트
    max_money = [0] * day
    max_money[0] = time_and_payment[0][1]

    for i in range(1, day):
        temp = 0
        for j in range(0, i):
            if((time_and_payment[j][2] <= i) and (max_money[j] >= temp)):
                temp = max_money[j]

        if(i+time_and_payment[i][0] <= day):
            max_money[i] = temp + time_and_payment[i][1]

    print(max(max_money))


'''
## 시간 초과 ##


    for i in range(day):
        if (i + time_and_payment[i][0] <= day):
            max_money[i + time_and_payment[i][0]] = max(
                max_money[i+time_and_payment[i][0]], max_money[i] + time_and_payment[i][1])
        max_money[i+1] = max(max_money[i+1], max_money[i])

    print(max_money[day])

'''
