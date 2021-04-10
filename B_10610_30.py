if __name__ == "__main__":
    numberSplit = list(input())
    # 내림차순 정렬
    numberSplit = sorted(numberSplit, key = lambda x : -int(x)) 
    answer = ''.join(numberSplit)

    numberSplit = list(map(int, numberSplit))
    # 30의 배수이려면 맨 뒤가 0이고 숫자 합이 3의 배수
    if(sum(numberSplit) % 3 == 0 and numberSplit[-1] == 0):
        print(int(answer))
    else:
        print(-1)