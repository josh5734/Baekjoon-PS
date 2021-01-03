
def solution(base, exp, div):
    # 지수가 1일때는 밑을 div로 나눈 값을 return
    if exp == 1:
        return base % div
    # 지수가 짝수일 때는 a^2n = a^n * a^n이고, (a*b)%c = (a%c) * (b%c) % c 임을 활용한다
    if exp % 2 == 0:
        r = solution(base, exp // 2, div)
        return (r * r) % div
    # 지수가 홀수일때는 지수에서 1을 빼서 짝수를 만드는 방식으로 logN 시간이 되도록 만들자.
    else:
        return (base * solution(base, exp-1, div)) % div


if __name__ == "__main__":
    # 밑, 지수, 나누기를 하는 수를 입력받는다.
    base, exp, div = map(int, input().split())

    rem = solution(base, exp, div)
    print(rem)
