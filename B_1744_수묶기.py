if __name__ == "__main__":
    n = int(input())
    positive, negative, one, zero = [], [], [], []
    for _ in range(n):
        number = int(input())
        if number == 1: one.append(number)
        elif number == 0 : zero.append(number)
        elif number < 0 : negative.append(number)
        elif number > 0 : positive.append(number)
    positive.sort()
    negative.sort(reverse = True)

    answer = 0
    # 양수는 최대한 큰 수끼리 묶는다
    while(len(positive) > 1):
        a = positive.pop()
        b = positive.pop()
        answer += a*b
    answer += sum(positive)

    # 음수는 절대값이 더 큰 수끼리 묶는다.
    while(len(negative) > 1):
        a = negative.pop()
        b = negative.pop()
        answer += a*b
    
    # 0이 있다면 남은 음수와 묶는다.
    for _ in range(len(zero)):
        if len(negative) != 0:
            negative.pop()    
    answer += sum(negative)

    # 1은 더한다.
    answer += len(one)

    print(answer)