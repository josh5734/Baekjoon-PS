N, K = map(int, input().split(" "))
arr = list(range(2, N+1))
cnt = 0


def filter(list):
    global cnt  # <- 전역변수 사용
    temp = 1
    start = list[0]
    number = start * temp
    while(number <= N):
        if(number in list):
            list.remove(number)
            cnt += 1
            # 탈출조건 --> 원하는 상황이 종료되게 만드는 것
            if(cnt == K):
                print(number)
                return
        else:
            continue
        temp += 1
    filter(list)


filter(arr)
