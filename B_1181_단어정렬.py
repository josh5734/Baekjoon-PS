import sys

if __name__ == "__main__":

    # 입력받을 단어의 개수 n개
    n = int(input())
    li = []
    for i in range(n):
        w = sys.stdin.readline().rstrip()
        if w not in li:
            li.append(w)

    # words_set를 문자열의 길이, 사전순으로 정렬
    li.sort(key=lambda x: (len(x), x))
    for word in li:
        print(word)
