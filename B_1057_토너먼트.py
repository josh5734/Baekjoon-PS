

def tournament(a, b, round):
    # kim이 홀수번째고, 그 바로 옆에 im이 오면 대결
    if a % 2 == 1 and b == a + 1:
        return round
    # im이 홀수번째고, 그 바로 옆에 kim이 오면 대결
    if b % 2 == 1 and a == b + 1:
        return round

    a = a // 2 if a % 2 == 0 else (a+1)//2
    b = b // 2 if b % 2 == 0 else (b+1)//2

    round += 1
    return tournament(a, b, round)


if __name__ == "__main__":
    n, kim, im = map(int, input().split())

    round = tournament(kim, im, 1)
    print(round)
