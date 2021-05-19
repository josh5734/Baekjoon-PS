
# 입력받기
a, p = map(int, input().split())

# 반복수열
series = [str(a)]

# 반복되는 수열의 길이 구하기
while True:
    pre, after = series[-1], 0

    # 각 자리수를 p제곱해서 더한다.
    for n in pre:
        after += int(n) ** p
    # 반복되는 부분이 있으면 처음 반복되는 수의 인덱스 전까지만 유효
    if str(after) in series:
        series = series[:series.index(str(after))]
        break
    else:
        series.append(str(after))
print(len(series))