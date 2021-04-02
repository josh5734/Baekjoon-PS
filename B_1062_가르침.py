from collections import defaultdict
from itertools import combinations as cb
import sys


def isIncluded(parent, child):
    for x in child:
        if x not in parent:
            return False
    return True


if __name__ == "__main__":
    n, k = map(int, input().split())

    alphabet = []
    for i in range(97, 97+26):
        if chr(i) not in ['a', 'n', 't', 'i', 'c']:
            alphabet.append(chr(i))

    word_list = []
    for _ in range(n):
        word = sys.stdin.readline().rstrip()
        word = list(filter(lambda x: x not in [
                    'a', 'n', 't', 'i', 'c'], word))
        word_list.append(word)

    check_alphabet = []
    for a in alphabet:
        for w in word_list:
            if a in w:
                check_alphabet.append(a)

    if k > 5:  # 최소 a,n,t,i,c는 배워야 함
        if len(check_alphabet) <= k-5:
            print(n)
        else:
            knownAlphabet = list(cb(check_alphabet, k-5))
            answer = 0
            for ka in knownAlphabet:
                canRead = 0
                for w in word_list:
                    if(isIncluded(ka, w)):
                        canRead += 1
                if canRead > answer:
                    answer = canRead
            print(answer)
    else:
        print(0)
