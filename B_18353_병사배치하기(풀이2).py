from bisect import bisect_left


def LIS(_list):
    dp = []
    for k in _list:
        idx = bisect_left(dp, k)  # lower bound
        if len(dp) <= idx:  # lower bound의 위치가 dp에서 맨 끝이라면 맨 마지막에 추가
            dp.append(k)
        else:  # lowerbound를 갱신
            dp[idx] = k
    return len(dp)


if __name__ == "__main__":
    n = int(input())
    soldier = list(map(int, input().split()))[::-1]  # 가장 긴 증가하는 부분 수열 문제로 변환
    length = LIS(soldier)
    print(n - length)
