a, b = map(int,input().split())
answer = 0

if a  == b:
    answer = 0
else:
    # a에서 b로 바꾸는 게 불가능한 경우
    # b 값이 홀수이면서 맨 마지막이 1이 아니면 불가능
    if b % 2 == 1 and str(b)[-1] != '1':
        answer = -2
    
    else:
        candidate = [a, a]
        flag = False
        while True:
            # 현재 수로 만들 수 있는 숫자는 2가지
            temp = []
            for i in range(len(candidate)):
                multiple = candidate[i] * 2 
                appendOne = candidate[i] * 10 + 1
                if b == multiple or b == appendOne:
                    flag = True
                    break
                else:
                    temp.append(multiple)
                    temp.append(appendOne)
            candidate = list(set(temp))

            # 짝수이지만 만들 수 없는 경우
            if min(candidate) > b:
                answer = -2
                break

            if flag:
                answer += 1
                break
            answer += 1
print(answer+1)