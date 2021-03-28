def makeTable(pattern):
    lp = len(pattern)
    table = [0]*lp  # 패턴의 길이와 같은크기의 테이블 생성
    i = 0  # i를 사용하여 테이블 값을 갱신한다
    for j in range(1, lp):
        # i와 j가 다르면 i는 i-1의 테이블값 인덱스로 돌아간다
        while i > 0 and pattern[i] != pattern[j]:
            i = table[i-1]  # 왜?->현재의 i에서 j와 다르니 i가 +1되었던것을 되돌아가서
            # i-1에서의 테이블값 인덱스에서 다시 j와 비교해준다
            # 테이블에는 최대 공통 부분들이 있어서 돌아갈지점을 계속 갱신해주다가
            # 0까지 가면 0이 된다.0을 저장하고 다음 j로 넘어간다

        if pattern[i] == pattern[j]:  # 만약 같으면 i값을 1더해주고 table값에 넣는다.
            i += 1  # i,j둘다 1씩 증가한다
            table[j] = i
    return table


def KMP(pattern, text):
    answer = []
    lt = len(text)
    lp = len(pattern)

    table = makeTable(pattern)
    i = 0
    for j in range(lt):
        while i > 0 and pattern[i] != text[j]:
            i = table[i-1]
        if pattern[i] == text[j]:
            if i == lp-1:
                answer.append(j-lp+2)
                i = table[i]
            else:
                i += 1
    return 1 if len(answer) > 0 else 0


if __name__ == "__main__":
    text = input().rstrip()
    pattern = input().rstrip()
    answer = KMP(pattern, text)
    print(answer)
