import sys
input = sys.stdin.readline


tc = int(input())

for _ in range(tc):
    n = int(input())
    phoneNum = [input().rstrip() for _ in range(n)]

    # 번호가 접두어라면 서로 연속된 위치에 위치한다.
    phoneNum.sort()
    flag = True
    for i in range(len(phoneNum)-1):
        # 다음 번호가 이전 번호로 시작한다면 일관성이 없는 전화번호임
        if phoneNum[i+1].startswith(phoneNum[i]):
            print("NO")
            flag = False
            break
    if flag:
        print("YES")


