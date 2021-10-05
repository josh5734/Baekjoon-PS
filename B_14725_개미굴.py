
class Trie:
    def __init__(self):
        self.root = Node("")

    def insertArray(self, arr):
        curr = self.root
        for food in arr:

            exist = False
            # 자식 노드에 값이 있다면 curr Node 위치만 수정
            for node in curr.childList:
                if node.value == food:
                    exist = True
                    curr = node
                    break
            # 자식 노드에 값이 없으면 해당 값을 value로 하는 노드를 삽입
            if not exist:
                curr.addChild(Node(food, curr.depth+1))
                # 사전 순으로 정렬
                curr.childList.sort(key = lambda x : x.value)
                # curr Node를 삽입한 노드로 변경
                for child in curr.childList:
                    if child.value == food:
                        curr = child
                        break

    def print(self):
        stack = [self.root]
        route = []
        while stack:
            curr = stack.pop()
            route.append((curr.value, curr.depth))
            temp = []
            # 앞에 위치한 자식부터 뽑기 위해 temp에는 맨 앞에 넣어야 함
            for child in curr.childList:
                temp.insert(0, child)
            for t in temp:
                stack.append((t))
        
        for r in route[1:]:
            print("--"*r[1] + r[0])

class Node:
    # 각 노드는 값, 깊이, 자식 리스트를 정보로 갖는다.
    def __init__(self, value, depth = -1):
        self.value = value
        self.depth = depth
        self.childList = []

    def addChild(self, node):
        self.childList.append(node)    

trie = Trie()
n = int(input())
for _ in range(n):
    line = input().split()
    k, foods = int(line[0]), line[1:]
    trie.insertArray(foods)
# DFS를 통해 결과 출력
trie.print()
