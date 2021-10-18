import sys
input = sys.stdin.readline

def wordsCount(knowingAlp):
    count = 0
    for w in words:
        # 모든 알파벳을 다 알고 있는 경우에 단어를 안다.
        if knowingAlp & w == w:
            count += 1
    print(count)

n, m = map(int, input().split())
words = [0 for _ in range(n)]
for i in range(n):
    word = input().strip()  # 각 단어를 알파벳 리스트로 받아서
    for w in word:
        words[i] |= 1 << ord(w) - 97  # 각 알파벳의 위치를 1로 만들기

# knowingAlp[i] = i번째 알파벳을 알고 있는지의 여부, 1 = 알고있음
knowingAlp = (1 << 26) - 1
for _ in range(m):
    o, x = input().split()
    idx = ord(x) - 97
    if o == '1': # 알파벳을 잊는다.
        knowingAlp &= ~(1 << idx)
    elif o == '2': # 알파벳을 기억한다.
        knowingAlp |= (1 << idx)
    
    # 해당 시점에 알고 있는 단어 수 출력
    wordsCount(knowingAlp)