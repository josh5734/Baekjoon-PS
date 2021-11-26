def makePassword(passwd, idx, p, q):
    # 모든 문자를 탐색했을 때
    if idx == len(letters):
        # 길이가 l이고 자음은 2자, 모음은 1자 이상이라면 성공
        if len(passwd) == l and p >= 2 and q >= 1:
            print(passwd)
        return
        
    curr = letters[idx]
    # 현재 문자를 포함, 미포함 둘 다 진행한다.
    # 포함한다면 현재 passwd에 문자를 더하고, 인덱스와 자음 or 모음의 개수를 증가시킨다.
    if curr in "aeiou":
        makePassword(passwd+curr, idx+1, p, q+1)
        makePassword(passwd, idx+1, p, q)
    else:
        makePassword(passwd+curr, idx+1, p+1, q)
        makePassword(passwd, idx+1, p, q)

l, c = map(int, input().split())
# 주어진 문자를 오름차순으로 정렬
letters = sorted(list(input().split()))
makePassword("", 0, 0, 0)

