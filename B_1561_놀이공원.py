import sys
if __name__ == "__main__":
    n, m = map(int, input().split())
    server = list(map(int, sys.stdin.readline().split()))
    # 최선, 최악의 상황을 끝점으로 이분탐색
    # 이 시간동안 N명이 놀이기구를 탈 수 있는지 확인
    left, right = 1, 60000000000
    time = 0
    idx = 0
    while left <= right:
        mid = (left + right) // 2

        # 각 놀이기구가 태울 수 있는 사람의 수
        count = 0
        for i in range(m):
            count += (mid - 1) // server[i] + 1

        # 더 많은 사람이 탈 수 있다면 시간 감축
        if count >= n:
            time = mid
            right = mid - 1
        else:
            left = mid + 1


    person = 0
    # 우선 time - 1분까지 놀이기구를 탄 사람을 더한다
    for i in range(m):
        person += (time-2) // server[i] +1
    
    answer = 0
    # time분째에서 사람을 한 사람씩 태워보면서 N번째 사람일 때 출력
    for i in range(m):
        if (time -1) % server[i] == 0:
            person += 1
            if person == n:
                answer = i + 1
                break
    print(answer)