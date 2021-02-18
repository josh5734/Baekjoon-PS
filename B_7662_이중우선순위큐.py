import sys
import heapq


def calculate(cal, num):
    global items

    if cal == "I":
        heapq.heappush(maxHeap, -num)
        heapq.heappush(minHeap, num)
        items += 1
        if not dic.get(num) or dic.get(num) == 0:
            dic[num] = 1
        else:
            dic[num] += 1

    if cal == "D":
        if items > 0:
            if num == 1:
                temp = heapq.heappop(maxHeap)
                dic[-temp] -= 1

            else:
                temp = heapq.heappop(minHeap)
                dic[temp] -= 1
            items -= 1
    print(minHeap)
    print(maxHeap)
    print(dic)
    print()


if __name__ == "__main__":
    # 테스트 케이스의 개수
    tc = int(input())

    for _ in range(tc):
        dic = dict()
        # 이중 우선순위 큐를 구현하기 위한 큐를 두개 생성
        items = 0
        maxHeap, minHeap = [], []

        answer_dic = {}
        # 연산의 개수 k
        k = int(input())
        for _ in range(k):
            line = sys.stdin.readline().split()
            cal, num = line[0], int(line[1])

            calculate(cal, num)

        if items == 0:
            print("EMPTY")
        else:
            for k in dic.keys():
                if dic[k] > 0:
                    answer_dic[k] = dic[k]
            print(f"{max(answer_dic)} {min(answer_dic)}")
