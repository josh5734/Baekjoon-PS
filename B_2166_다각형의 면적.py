import sys
input = sys.stdin.readline

n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]

# 마지막에 첫 x, y좌표를 붙여준다.
points.append(points[0])

answer = 0
# 오른쪽 대각선 방향으로 곱한 값들에서 왼쪽 대각선 곱한 값들을 뺀다.
for i in range(len(points)-1):
    answer += points[i][0] * points[i+1][1]
    answer -= points[i+1][0] * points[i][1]

print(round(abs(answer) / 2, 1))
