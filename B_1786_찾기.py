# KMP Algorithm 사용
import sys


def findLPS(target, lps):
    # lps 초기화
    l = 0

    # target 문자열의 첫 문자의 lps = 0 // target문자열이 두번째 문자열부터 탐색 시작
    cursor = 1

    while cursor < len(target):
        # 이전 인덱스에서 시작과 끝이 같으면 다음 인덱스를 비교
        if target[cursor] == target[l]:
            l += 1
            lps[cursor] = l
            cursor += 1
        # 일치하지 않는다면 다음 인덱스로 넘어간다
        else:
            # 그 이전 인덱스는 일치했었다면 l을 줄여서 다시 확인
            if l != 0:
                l = lps[l-1]
            else:
                lps[cursor] = 0
                cursor += 1
    return lps


if __name__ == "__main__":
    # 주어진 문자열, 찾을 문자열
    str = sys.stdin.readline().rstrip()
    target = sys.stdin.readline().rstrip()

    # 문자열 일치 부분을 담을 리스트
    find_pattern_index = []

    l_target = len(target)
    l_str = len(str)
    # prefix, suffix가 일치하는 부분의 길이 정보를 담는 lps 리스트
    lps = [0]*l_target
    lps = findLPS(target, lps)

    # str, target 문자열의 커서 위치
    i, j = 0, 0
    while i < l_str:
        # 문자열이 같으면 str, target의 커서를 오른쪽으로 이동해가면서 확인
        if str[i] == target[j]:
            i += 1
            j += 1
        # 문자열이 다르면
        elif str[i] != target[j]:
            if j != 0:
                j = lps[j-1]
            else:
                i += 1

        # pattern을 찾은 경우
        if j == l_target:
            find_pattern_index.append(i-j+1)
            j = lps[j-1]

    print(len(find_pattern_index))
    for idx in find_pattern_index:
        print(idx, end=' ')
