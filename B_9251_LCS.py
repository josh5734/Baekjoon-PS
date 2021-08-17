import sys


if __name__ == "__main__":
    # 두 문자열 입력받기
    s1 = sys.stdin.readline().rstrip()
    s2 = sys.stdin.readline().rstrip()

    length = len(s1)

    # s1의 각 문자가 s2의 어디에 존재하는지를 기록
    charLocation = [[] for _ in range(len(s1))]
    for i in range(length):
        for j in range(len(s2)):
            if s1[i] == s2[j]:
                charLocation[i].append(j)
        if len(charLocation[i]) == 0:
            charLocation[i].append(-1)
    print(charLocation)
    LCS = [0] * length

    for i in range(1, length):
        temp = max(charLocation[i])
        count = 0
        for j in range(i-1, -1, -1):
            for idx in charLocation[j][::-1]:
                if idx != -1 and idx < temp:
                    count += 1
                    temp = idx
                    break
        LCS[i] += count
    if max(LCS) != 0:
        print(max(LCS)+1)
    else:
        print(0)
