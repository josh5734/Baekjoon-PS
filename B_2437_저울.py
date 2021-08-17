import sys


if __name__ == "__main__":

    n = int(input())
    pend = list(map(int, sys.stdin.readline().split()))
    pend.sort()

    # 측정할 수 있는 무게를 맨 처음 = 0으로 설정
    weight = [0]

    # 그전까지 측정할 수 있는 무게에서 최대값과 현재 가지고 있는 추의 무게를 비교해서 1보다 차이가 크면 끝남
    for p in pend:
        if p - weight[-1] > 1:
            break
        else:
            # 측정할 수 있는 가장 큰 무게만 기록하기
            weight.append(p+weight[-1])

    # 결과 출력
    print(weight[-1]+1)

