n = int(input())
for i in range(1, n+1):  # 1 2 3 4 ... n-1
    str = " " * (n-i) + "*"*i
    print(str)
