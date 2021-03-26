import math
# 에라토스테네스의 체


def eratos():
    isPrime = [True] * 10001
    isPrime[1] = False
    for i in range(2, int(math.sqrt(10001))+1):
        if isPrime[i]:
            temp = 2
            while i * temp < 10001:
                isPrime[i*temp] = False
                temp += 1
    return isPrime


if __name__ == "__main__":
    m = int(input())
    n = int(input())

    isPrime = eratos()

    total = 0
    for i in range(m, n+1):
        if isPrime[i]:
            total += i
    if total == 0:
        print(-1)
    else:
        print(total)
        print(isPrime[m:n+1].index(True) + m)
