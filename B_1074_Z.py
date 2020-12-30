
def divide(section_size, r, c):
    global count
    section_size //= 2
    # 탈출 조건
    if section_size == 1:
        q1, q2 = r % 2, c % 2

        if q1 == 0 and q2 == 0:
            count += 0
        elif q1 == 0 and q2 == 1:
            count += 1
        elif q1 == 1 and q2 == 0:
            count += 2
        else:
            count += 3
        return count

    else:
        if section_size > r and section_size > c:
            section = 1
        elif section_size > r and section_size <= c:
            section = 2
            c -= section_size
        elif section_size <= r and section_size > c:
            section = 3
            r -= section_size
        else:
            section = 4
            r -= section_size
            c -= section_size

        # 이전 사분면까지 있는 숫자들의 개수를 더한다.
        count += (section-1) * (section_size ** 2)

        return divide(section_size, r, c)


if __name__ == "__main__":
    n, r, c = map(int, input().split())
    count = 0

    # 몇번째 사분면인지 구하기 위한 section 변수
    section = 0
    original_size = 2**n
    divide(original_size, r, c)

    print(count)
