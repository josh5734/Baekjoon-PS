import math


if __name__ == "__main__":
    n = int(input())
    # 에라토스테네스의 체
    isPrime = [True] * 1001
    isPrime[1] = False
    for i in range(2, int(math.sqrt(1001))+1):
        if isPrime[i] == True:
            for j in range(i*2, 1001, i):
                isPrime[j] = False

    answer = 0
    for number in set(list(map(int, input().split()))):
        if isPrime[number]:
            answer += 1

    print(answer)
