from itertools import combinations as C
import sys

# 지금 배운 알파벳으로 몇 단어를 읽을 수 있는지 리턴하는 함수
def countReadableWords(words, learned):
	count = 0
	for word in words:
		canRead = True
		for w in word:
            # 배우지 않은 알파벳이 있다면 False
			if learned[ord(w)] == False:
				canRead = False
				break
		if canRead:
			count += 1
	return count

n, k = map(int, input().split())
answer = 0
# a,n,t,i,c는 반드시 가르쳐야 함
alphabet = set(chr(i) for i in range(97, 123)) - {'a','n','t','i','c'}
words = [sys.stdin.readline().rstrip()[4:-4] for _ in range(n)]

if k >= 5:
	learned = [False] * (150)
	for x in {'a','n','t','i','c'}:
		learned[ord(x)] = True
	# 남은 알파벳 중에서 k-5개를 선택해본다.
	for teach in list(C(alphabet, k-5)):
		for t in teach:
			learned[ord(t)] = True
		count = countReadableWords(words, learned)
		if count > answer:
			answer = count
        # 배운 단어 초기화
        for t in teach:
			learned[ord(t)] = False
	print(answer)
else:
	print(0)