n, k = map(int, input().split())
num = input()
answer = ""
for n in num:
    if len(answer) == 0: 
        answer += n
    else:
        while(len(answer) > 0 and k > 0 and answer[-1] < n):
            answer = answer[:-1]
            k -= 1
        answer += n
if k > 0: answer = answer[:-k]
print(answer)