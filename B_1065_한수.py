if __name__ == "__main__":
    n = int(input())
    answer = 0

    for num in range(1, n+1):

        # 두자릿수 이하면 무조건 등차수열
        if num <= 99:
            answer += 1
        else:
            num = list(map(int, (str(num))))
            if num[2] - num[1] == num[1] - num[0]:
                answer += 1
    print(answer)
