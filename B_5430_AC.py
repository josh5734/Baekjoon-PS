import sys
from collections import deque




tc = int(input())
for _ in range(tc):
    # 수행할 함수, 수의 개수, 배열 입력받기
    operation = sys.stdin.readline().rstrip()
    length = int(sys.stdin.readline().rstrip())
    
    # num_array는 string으로 들어오기 때문에 리스트 형태로 바꾸기
    num_array = sys.stdin.readline().rstrip()[1:-1].split(',')
    error_flag = False
    # 아무것도 없는 리스트일 경우 [""} 형태로 저장되고, 이 때는 빈 리스트로 치환
    if num_array[0] == "":
        num_array = []

    # 큐 형태로 만든다.
    q = deque(map(int,num_array))

    # 매번 실제로 큐를 뒤집지 않고 isReversed 상태에 따라
    # "D" 명령을 할 때, 앞에서 뺄지 뒤에서 뺄지 결정하고
    # 마지막에 출력할 때 Reverse 1회 수행
    isReversed = 1


    for op in operation:
        # R 명령인 경우 상태 변환
        if op == "R":
            isReversed *= -1
        # D 명령인 경우 버리기
        elif op == "D":
            if len(q) == 0:
                error_flag = True
                break
            else:
                if isReversed == 1:
                    q.popleft()
                elif isReversed == -1:
                    q.pop()
    if error_flag:
        print("error")
    else:
        if isReversed == -1:
            q.reverse()
        # 공백 없이 출력하기
        print('[', end = "")
        for i in range(len(q)):
            if i == len(q) - 1:
                print(q[i], end = "")
            else:
                print(q[i], end = ",")
        print(']')