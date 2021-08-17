
if __name__ == "__main__":
    s = input()
    oneToZero, ZeroToOne = 0, 0

    one, zero = True, True
    # 0을 1로 바꿔야하는 경우
    for i in range(len(s)):
        if one and s[i] == '0':
            oneToZero += 1
            one = False
        elif s[i] == '1':
            one = True

    # 1을 0으로 바꿔야하는 경우
    for i in range(len(s)):
        if zero and s[i] == '1':
            ZeroToOne += 1
            zero = False
        elif s[i] == '0':
            zero = True
    print(min(oneToZero, ZeroToOne))
