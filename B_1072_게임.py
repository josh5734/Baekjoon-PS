

if __name__ == "__main__":
    answer = 0
    x, y = map(int, input().split())

    z = int(100*y/x)

    left, right = 1, x
    while left <= right:
        mid = int((left+right)/2)

        if int(100*(y+mid)/(x+mid)) <= z:
            left = mid + 1
        else:
            right = mid - 1
            answer = mid
    if answer == 0:
        print(-1)
    else:
        print(answer)
