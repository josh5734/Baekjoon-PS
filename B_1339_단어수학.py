
############ 시간초과 ##########
from itertools import permutations as p

if __name__ == "__main__":
    answer = 0

    # 주어지는 단어의 수
    n = int(input())

    words = [[] for _ in range(n)]

    # 가장 긴 길이를 가지는 단어를 기록
    length = 0
    # 주어진 단어들을 리스트로 닮기
    for i in range(n):
        word = input()
        # 수의 최대 길이를 8로 제한
        if len(word) > 8:
            word = word[:8]
        for j in range(len(word)):
            words[i].append(word[j])
        if len(word) >= length:
            length = len(word)

    # 단어들을 배치하는 경우의 수를 순열로 구함
    pm = list(p(words, len(words)))

    for p in pm:
        if len(p[0]) != length:
            continue
        # 각 단어에 해당하는 숫자를 저장하는 dictionaray 생성
        words_num = {}
        # 가장 앞 자릿수에 부여되는 숫자를 9로 시작
        start = 9

        # 자릿수에 맞춰서 정렬하기
        for x in p:
            while len(x) < 8:
                x.insert(0, '')
        # 높은 자릿수부터 자연수 9부터 내려가면서 배정
        for i in range(8):
            for x in p:
                if x[i] != '' and not words_num.get(x[i]):
                    words_num[x[i]] = start
                    start -= 1
        temp = 0
        for x in p:
            for i in range(8):
                if x[i] != '':
                    temp += words_num[x[i]] * (10 ** (7 - i))
        if answer <= temp:
            answer = temp

    print(answer)
