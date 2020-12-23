if __name__ == "__main__":
    # 버튼 누르는 시간, 같은 숫자인 문자를 누르는 데 기다리는 시간
    p, w = map(int, input().split())
    # 주어지는 문자열
    str = input()
    # 다이얼 정보
    b1 = [" "]
    b2 = ["A", "B", "C"]
    b3 = ["D", "E", "F"]
    b4 = ["G", "H", "I"]
    b5 = ["J", "K", "L"]
    b6 = ["M", "N", "O"]
    b7 = ["P", "Q", "R", "S"]
    b8 = ["T", "U", "V"]
    b9 = ["W", "X", "Y", "Z"]
    buttons = [b1, b2, b3, b4, b5, b6, b7, b8, b9]

    time = 0
    # 처음 커서 위치는 공백에 위치
    cursor = b1
    for c in str:
        for b in buttons:
            if c in b:
                # 같은 버튼 안에 문자가 위치할 때 / 공백을 연속으로 입력할 때는 기다리지 않음
                if cursor == b and c != " ":
                    time += w + (cursor.index(c)+1) * p
                    break
                # 커서가 이동할 때
                else:
                    cursor = b
                    time += (cursor.index(c)+1) * p

    # 문자열의 처음은 공백이 아니므로 커서를 처음에 이동하는 시간은 제외
    print(time)
