def notUseAnymoreItem():
    for i in range(n):
        if multitap[i] not in item:
            return i
    return -1


def getLastUsedItem():
    deleteIndex = 0
    time = []
    for i in range(n):
        for j in range(len(item)):
            if multitap[i] == item[j]:
                time.append(j)
                break
    LastUseTime = max(time)
    deleteIndex = time.index(LastUseTime)
    return deleteIndex


if __name__ == "__main__":
    n, k = map(int, input().split())
    item = list(map(int, input().split()))
    multitap = []
    count = 0                       # 멀티탭 뽑는 횟수
    plugInCount = 0                 # 꽂혀 있는 제품 수
    while item:
        curr = item.pop(0)
        # 이미 꽂혀있는 제품일 경우 그냥 사용
        if curr in multitap:
            continue
        # 아직 멀티탭 자리가 남은 경우
        else:
            if plugInCount < n:
                multitap.append(curr)
                plugInCount += 1
            else:  # 어느 하나를 뽑아야 하는 경우
                if notUseAnymore() != -1:
                    deleteIndex = notUseAnymoreItem()
                else:
                    deleteIndex = getLastUsedItem()
                count += 1
                multitap.pop(deleteIndex)
                multitap.append(curr)
    print(count)
