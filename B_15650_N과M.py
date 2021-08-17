from itertools import combinations as c


if __name__ == "__main__":
    n, m = map(int, input().split())

    # 1부터 n까지 수를 담는 리스트
    numbers = [i for i in range(1, n+1)]

    # 1부터 n까지 중복 없이 m개를 고른 수열
    sequence = list(c(numbers, m))

    # 결과 출력
    for s in sequence:
        for l in range(len(s)):
            print(s[l], end=' ')
        print()
