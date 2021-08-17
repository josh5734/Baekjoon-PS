import sys

n = int(input())
series = list(map(int, sys.stdin.readline().split()))
answer = [-1] * n # 각 숫자의 오큰수를 저장하는 리스트

# n = 1 이면 -1 출력하고 끝
if n == 1:
    print(-1)
else:
    stack = [[series[0], 0]] # 맨 처음 수의 값과 인덱스를 stack에 넣고 시작
    for i in range(1, n):
        while stack and stack[-1][0] < series[i]:   # 오큰수를 찾으면 스택에 있는 값들을 다시 빼낸다.
            answer[stack[-1][1]] = series[i]
            stack.pop()
        stack.append([series[i], i])    # 오큰수를 찾지 못하면 stack에 삽입

    for n in answer:
        print(n, end = ' ')


'''
## 시간 초과 ##
def findNGE(series, n):
    for num in series:
        if num > n:
            return num
    return -1

n = int(input())
series = list(map(int, sys.stdin.readline().split()))

answer = []
# 맨 처음 수에 대한 오큰수 구하기
temp = findNGE(series[1:], series[0])
answer.append(temp)

for i in range(1, n):
    # 마지막 수
    if i == n-1:
        answer.append(-1)
    elif series[i] >= series[i-1] and temp > series[i]:
        answer.append(temp)
    else:
        temp = findNGE(series[i+1:], series[i])
        answer.append(temp)

for n in answer:
    print(n, end = ' ')
'''