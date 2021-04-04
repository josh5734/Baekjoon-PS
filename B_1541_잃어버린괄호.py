if __name__ == "__main__":
    text = input() 
    numbers = []
    ops = []
    temp = ""
    # 숫자랑, 더하기빼기 분리   
    for i in range(len(text)):
        if text[i].isdigit():
            temp += text[i]
        else:
            numbers.append(int(temp))
            ops.append(text[i])
            temp = ""
    numbers.append(int(temp))    # 마지막 숫자 삽입

    result = numbers[0]
    cursor = 1
    temp = 0
    # (-)를 만나면 (+)가 나오는 때는 계속 누적해서 뺀다. 
    while cursor < len(numbers):
        temp = numbers[cursor]
        if ops[cursor-1] == '-':
            while(cursor < len(ops) and ops[cursor] == '+'):
                temp += numbers[cursor+1]
                cursor += 1
            cursor += 1
            result -= temp
            temp = 0
        else:
            result += numbers[cursor]
            cursor += 1    
    print(result)


