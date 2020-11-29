def find_apt_group(graph, x, y, apt_info, danzi):
    count = 0
    # 단지 범위를 벗어나면 false
    if x <= -1 or x >= n or y <= -1 or y >= n:
        return False

    # 만약 해당 좌표에 집이 있다면
    if graph[x][y] == 1:
        # 집의 수를 1씩 늘린다.
        apt_info[danzi] += 1
        # 방문 체크를 해준다.
        graph[x][y] = 0
        find_apt_group(graph, x-1, y, apt_info, danzi)
        find_apt_group(graph, x+1, y, apt_info, danzi)
        find_apt_group(graph, x, y-1, apt_info, danzi)
        find_apt_group(graph, x, y+1, apt_info, danzi)

        return True
    return False


if __name__ == "__main__":
    n = int(input())

    # 아파트 단지 번호와 인원
    apt_info = [0 for i in range(n**2)]
    danzi = 1

    # 아파트 정보 입력받기
    graph = []
    for i in range(n):
        graph.append(list(map(int, input())))

    for x in range(n):
        for y in range(n):
            if find_apt_group(graph, x, y, apt_info, danzi) == True:
                danzi += 1

    # 아파트 단지 정보에서 0이 아닌 값의 개수만 출력 = 아파트 총 단지 수
    print(len(apt_info) - apt_info.count(0))
    # 아파트 단지별로 세대수를 출력하고, 0이 나타나면 그 뒤의 단지가 없기 때문에 종료
    house_number = []
    for i in range(1, len(apt_info)):
        if apt_info[i] != 0:
            house_number.append(apt_info[i])
        else:
            break
    # 오름차순으로 출력
    for x in sorted(house_number):
        print(x)
