






if __name__ == "__main__":
    text = input() 
    numbers = []
    ops = []
    temp = ""
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