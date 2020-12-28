import sys


if __name__ == "__main__":
    # 문자열 입력받기
    str = sys.stdin.readline().rstrip()

    # 문자열을 쌓을 stack
    stack = []

    # 폭발 문자열, 폭발 문자열의 길이
    bomb = sys.stdin.readline().rstrip()
    b_length = len(bomb)

    for w in str:
        # 만약 폭발 문자열의 길이가 1이라면 집어 넣을 때 확인
        if b_length == 1:
            if w == bomb:
                continue
            else:
                stack.append(w)
        # 폭발 문자열의 길이가 2이상이면, 이미 넣은 스택의 뒷부분 값과 현재 넣을 값을 더해서 비교
        else:
            if len(stack) < b_length-1:
                stack.append(w)
            else:
                temp = ''.join(stack[-(b_length-1):])
                if temp + w == bomb:
                    del stack[-(b_length-1):]
                else:
                    stack.append(w)
    answer = ''.join(stack)
    print("FRULA" if answer == "" else answer)
    '''
    # 순회를 하면서 bomb 문자열을 탐색할 cursor
    cursor = 0

    str_length = len(str)
    bomb_length = len(bomb)
    while cursor <= str_length - bomb_length:
        # bomb 문자열을 발견했을 때
        if str[cursor:cursor+bomb_length] == bomb:
            str = str.replace(bomb, "")
            # 커서가 시작 위치가 아니라면 문자열을 삭제하고 커서를 한 칸 앞으로 당긴다.
            if cursor == 0:
                continue
            else:
                cursor -= (bomb_length - 1)
        else:
            cursor += 1
    print("FRULA" if str == "" else str)
    '''
