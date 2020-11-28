
if __name__ == "__main__":
    # 수의 길이
    n = int(input())

    # 길이가 N이고 마지막 자릿수를 저장
    numbers = [[0 for i in range(10)] for i in range(100)]

    # 길이가 1일 때 초기화
    for i in range(1, 10):
        numbers[0][i] = 1
        
    for i in range(1, n):
        for j in range(10):
            # 맨 뒷자리가 0가 되려면 이전 값이 1
            if j == 0:
                numbers[i][j] = numbers[i-1][1]
            # 맨 뒷자리가 9가 되려면 이전 값이 8
            elif j == 9:
                numbers[i][j] = numbers[i-1][8]
            # 그 외의 경우는 해당 값 +- 1
            else:
                numbers[i][j] = numbers[i-1][j-1] + numbers[i-1][j+1]

    print(sum(numbers[n-1]) % 1000000000)
