import sys


if __name__ == "__main__":
    tc = int(input())

    for _ in range(tc):
        m = int(input())
        sequence = []
        mid_list = []
        # 입력이 몇 줄인지 계산하는 itr 변수
        itr = m // 10 if m % 10 == 0 else m // 10 + 1

        # 수열 정보 입력받기
        count = 0
        for _ in range(itr):
            for num in list(map(int, sys.stdin.readline().split())):
                # 숫자를 sequence에 넣으면서 홀수번째마다 정렬 후 중앙값을 mid_list에 삽입
                sequence.append(num)
                count += 1
                if count % 2 == 1:
                    mid_list.append(sorted(sequence)[len(sequence)//2])

        # 결과 출력
        length = len(mid_list)
        print(length)
        enter = 0
        for n in mid_list:
            print(n, end=' ')
            enter += 1
            if enter == 10:
                print()
                enter = 0
