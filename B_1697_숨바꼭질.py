from collections import deque


def search(x, k, cnt):
    # 방문할 위치들을 기록
    q = deque()

    # 방문했던 위치 기록을 하여 중복 제거
    visited = [False] * 100001

    # 시작
    q.append(x)

    while True:
        # 찾고자 하는 k값이 stack 안에 존재하면 탈출
        if k in q:
            return cnt

        # 3가지 이동결과를 stack에 넣고 cnt를 1씩 증가
        cnt += 1
        temp = []
        while q:
            temp.append(q.popleft())
            visited[temp[-1]] = True

        # temp에 넣을 값은 이미 방문한 적이 없고, 문제의 조건 100,000보다 작아야 함
        for i in range(len(temp)):
            # 앞 부분에 x에 대한 범위조건을 걸어줘야 뒤의 visited의 인덱스 크기를 초과하지 않음
            if temp[i]+1 >= 0 and temp[i]+1 <= 100000 and not visited[temp[i]+1]:
                q.append(temp[i]+1)
            if temp[i]-1 >= 0 and temp[i]-1 <= 100000 and not visited[temp[i]-1]:
                q.append(temp[i]-1)
            if temp[i]*2 >= 0 and temp[i]*2 <= 100000 and not visited[temp[i]*2]:
                q.append(temp[i]*2)


# 메인 함수
if __name__ == "__main__":
    # n, k 입력
    n, k = map(int, input().split())

    # 내 위치가 동생보다 앞에 있으면 뒤로 이동할 수밖에 없음
    if n > k:
        print(n-k)
    else:
        # n번째 탐색 결과 -> result
        print(search(n, k, 0))
