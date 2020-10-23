total = int(input())
times = [300, 60, 10]
answer = [0, 0, 0]

if(total % 10 != 0):
    print(-1)
else:
    for i in range(3):
        if(total >= times[i]):
            answer[i] += total // times[i]
            total %= times[i]
    print(str(answer[0]) + " " + str(answer[1]) + " " + str(answer[2]))
