import sys

source, target= map(int, sys.stdin.readline().split())

if source == target:
    print(1)
else:
    count = 1
    found = False
    while target > source:
        # 현재 타겟값의 맨 뒤가 1이면 무조건 1을 빼봐야 한다.
        if str(target)[-1] == '1':
            target = (target - 1) // 10
            count += 1
            if target == source:
                found = True
                print(count)  
                break      
        if target % 2 == 0:
            target //= 2
            count += 1
            if target == source:
                found = True
                print(count)
                break      

        # 현재 타겟값이 홀수인데 마지막도 1이 아니면 불가능해진다.
        if target % 2 == 1 and str(target)[-1] != '1':
            break
    
    # 불가능하다면 -1 출력
    if not found:
        print(-1)

''' 메모리 초과'
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
            if flag:
                answer += 1
                break
            if min(candidate) > b:
                answer = -2
                break
            answer += 1
print(answer+1)
'''
