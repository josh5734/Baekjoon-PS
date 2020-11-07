# 데이터의 개수가 1,000,000개 / 음수 존재 --> 음수를 처리하기 위해 1,000,000을 더하고 시작
# 메모리가 상당히 비효율적 / 시간 문제..??
if __name__ == "__main__":
     n = int(input())
    numbers = []

    count = [0] * 2000001
    # 숫자를 입력받음
    for i in range(n):
        numbers.append(int(input())+1000000)

    for i in range(len(numbers)):   
        count[numbers[i]] = 1

    for i in range(len(count)):
        if count[i] == 1:
            print(i-1000000)
