from math import factorial

n = int(input())
# 팩토리얼을 스트링으로 만든 후 거꾸로
factorial_str = str(factorial(n))[::-1]

# 처음으로 0이 아닌 수 등장하면 종료
for i in range(len(factorial_str)):
    if factorial_str[i] != '0':
        print(i)
        break