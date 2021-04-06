if __name__ == "__main__":
    height, width = map(int, input().split())
    answer = 0
    # 높이가 1, 2, 3일때 따라 그림이 달라짐
    if height == 1: 
        answer = 1
    elif height == 2:   
        if width <= 2:
            answer = 1
        elif 3<= width <= 4:
            answer = 2
        elif 5 <= width <= 6:
            answer = 3
        else:
            answer = 4
    else:
        if width <= 6:
            answer = min(4, width)
        elif width >= 7 :   # 7이상부터 4번 이동 가능
            answer = width - 2
    print(answer)