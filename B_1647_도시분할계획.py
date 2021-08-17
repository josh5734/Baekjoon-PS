# Using kruskal algorithm
import sys


def find_parent(parent, x):
    # 루트 노드가 아니라면 루트 노드를 찾을 때 까지 재귀적으로 호출
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


if __name__ == "__main__":
    # 마을, 간선 개수
    n, e = map(int, input().split())

    # 부모 테이블 초기화
    parent = [0] * (n + 1)
    for i in range(1, n+1):
        parent[i] = i

    # 모든 간선을 담을 리스트와 최종 비용을 담을 변수
    result = 0
    edges = []

    # 모든 간선에 대한 정보 입력받기
    for _ in range(e):
        sour, dest, cost = map(int, sys.stdin.readline().split())
        # 비용 순으로 정렬하기 위해 튜플의 첫 번째 원소를 비용으로 설정
        edges.append((cost, sour, dest))

    # 간선을 비용순으로 정렬
    edges.sort()

    max_cost = 0

    for edge in edges:
        cost, sour, dest = edge
        # 사이클이 발생하지 않는 경우메나 집합에 포함
        if find_parent(parent, sour) != find_parent(parent, dest):
            union_parent(parent, sour, dest)
            result += cost
            # 맨 마지막으로 선택되는 간선이 비용이 가장 높은 간선
            max_cost = cost

    # 마을을 가장 큰 간선 비용을 기준으로 2개로 분할
    answer = result - max_cost
    print(answer)
