import math
if __name__ == "__main__":
    a, b = map(int, input().split())
    gcd = math.gcd(a, b)
    minV, maxV = min(a, b), max(a, b)
    cnt = 1
    while True:
        if (minV * cnt) % maxV == 0:
            break
        cnt += 1

    print(gcd)
    print(minV * cnt)
