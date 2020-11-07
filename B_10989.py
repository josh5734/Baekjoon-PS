import sys

# 데이터의 개수가 10,000,000개 / 1부터 10000까지 -> 계수정렬
if __name__ == "__main__":
    n = int(input())
    count = [0] * 10001
    # 숫자를 입력받음
    for i in range(n):
        # 입력값이 많은 경우 input()을 이용해 받으면 시간이 오래걸린다.
        # sys.stdin.readlin()을 통해 입력받는다.
        count[int(sys.stdin.readline())] += 1

    for i in range(10001):
        while(count[i] != 0):
            print(i)
            count[i] -= 1
