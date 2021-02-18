

if __name__ == "__main__":
    n = int(input())
    k = int(input())

    sqr = []
    for i in range(1, n+1):
        sqr.append(i**2)

    start = 0
    for i in range(1, len(sqr)):
        if sqr[i-1] <= k and sqr[i] >= k:
            start = i
            break

    part = []
    for i in range(1, start+2):
        part.append((start+1) * i)
        part.append((start+1) * i)
    part.pop()
    location = k - start ** 2 - 1
    answer = part[location]

    print(answer)
