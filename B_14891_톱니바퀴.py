import sys

def show(circle):
    for i in range(len(circle)):
        for s in circle[i]:
            print(s, end = ' ')
        print()

def rotateRight(array):             
    temp = array[:-1]
    temp.insert(0,array[-1])
    return temp

def rotateLeft(array):
    temp = array[1:]
    temp.append(array[0])
    return temp

if __name__ == "__main__":
    circle = []
    for _ in range(4):
        circle.append(list(map(int, sys.stdin.readline().rstrip())))

    
    k = int(input())
    # k번 회전
    for _ in range(k):
        idx, direction = map(int, input().split())
        idx -= 1
        directionOfCircle = [0,0,0,0]
        directionOfCircle[idx] = direction

        for i in range(idx, 0, -1):
            if (circle[i][6] != circle[i - 1][2]):
                directionOfCircle[i-1] = -directionOfCircle[i]
            else:
                break
        for i in range(idx, 3):
            if circle[i][2] != circle[i+1][6]:
                directionOfCircle[i + 1] = -directionOfCircle[i];
            else:
                break

        for i in range(4):
            if directionOfCircle[i] == -1:
                circle[i] = rotateLeft(circle[i])
            elif directionOfCircle[i] == 1:
                circle[i] = rotateRight(circle[i])
    show(circle)
    answer = 0
    for i in range(4):
        answer += (2**i)*circle[i][0]
    print(answer)