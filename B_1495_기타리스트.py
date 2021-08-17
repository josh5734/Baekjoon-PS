# 곡의 개수, 시작 볼륨, 최대 볼륨
n, s, m = map(int, input().split())
volume_list = list(map(int, input().split()))

#dp[i][j] = i번째 곡을 볼륨 j로 연주할 수 있는가?
dp = [[False] * (m+1) for _ in range(n)]

# 처음 곡의 가능한 볼륨 초기화
if  s + volume_list[0] <= m:
    dp[0][s + volume_list[0]] = True
if  s - volume_list[0] >= 0:
    dp[0][s - volume_list[0]] = True 


for i in range(1, n):
    for j in range(m+1):
        if dp[i-1][j] == True:
            if j + volume_list[i] <= m:
                dp[i][j + volume_list[i]] = True
            if j - volume_list[i] >= 0:
                dp[i][j - volume_list[i]] = True

max_volume = -1
for idx, available in enumerate(dp[n-1]):
    if available: max_volume = idx

print(max_volume)

''' 
// 백트래킹 -> 시간초과 
def backTracking(currVolume, index):
    global answer

    # 가지치기
    if currVolume > m or currVolume < 0:
        return

    # 마지막 곡 
    if index == n:
        if answer < currVolume:
            answer = currVolume
        return

    backTracking(currVolume - volume_list[index], index + 1)
    backTracking(currVolume + volume_list[index], index + 1)

# 곡의 개수, 시작 볼륨, 최대 볼륨
n, s, m = map(int, input().split())
volume_list = list(map(int, input().split()))

answer = -1
backTracking(s, 0)
print(answer)
'''