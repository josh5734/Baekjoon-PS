import sys


if __name__ == "__main__":
    answer = 0
    n, m = map(int, input().split())
    dictionary = {}

    for _ in range(n):
        word = sys.stdin.readline()
        dictionary[word] = 1

    for _ in range(m):
        test = sys.stdin.readline()
        if test in dictionary:
            answer += 1
    print(answer)
