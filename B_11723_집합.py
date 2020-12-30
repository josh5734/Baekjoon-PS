import sys


if __name__ == "__main__":
    m = int(input())

    dic = dict()
    for i in range(1, 21):
        dic[i] = 0
    for _ in range(m):
        row = sys.stdin.readline().split()
        if row[0] == "all":
            for k in dic.keys():
                dic[k] = 1
        elif row[0] == "empty":
            for k in dic.keys():
                dic[k] = 0
        else:
            do, number = row[0], int(row[1])
            if do == "add":
                dic[number] = 1
            elif do == "check":
                if dic[number] == 1:
                    print(1)
                else:
                    print(0)
            elif do == "remove":
                dic[number] = 0
            elif do == "toggle":
                dic[number] = 1 if dic[number] == 0 else 0
