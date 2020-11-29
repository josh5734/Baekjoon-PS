import sys

if __name__ == "__main__":
    # 입력받을 회원의 수 n명
    n = int(input())
    li = []
    for i in range(n):
        age, name = sys.stdin.readline().split()
        li.append((int(age), name))

    # 나이순서로 정렬하고, 그 외는 입력받은 순서대로
    li.sort(key=lambda x: x[0])
    for info in li:
        print(info[0], info[1])
