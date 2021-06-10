from collections import defaultdict

class Node:
    def __init__(self, data, left, right):
        self.data = data;
        self.left =  left;
        self.right = right;

    def getData(self):
        return self.data
    
    def getLeftChild(self):
        return self.left

    def getRightChild(self):
        return self.right


def preoder_traverse(node):
    print(node.getData(), end ='')
    if(node.getLeftChild() != '.'):
        preoder_traverse(tree[node.getLeftChild()])
    if(node.getRightChild() != '.'):
        preoder_traverse(tree[node.getRightChild()])
        


def inorder_traverse(node):
    if(node.getLeftChild() != '.'):
        inorder_traverse(tree[node.getLeftChild()])
    print(node.getData(), end ='')
    if(node.getRightChild() != '.'):
        inorder_traverse(tree[node.getRightChild()])

def postorder_traverse(node):
    if(node.getLeftChild() != '.'):
        postorder_traverse(tree[node.getLeftChild()])
    if(node.getRightChild() != '.'):
        postorder_traverse(tree[node.getRightChild()])
    print(node.getData(), end ='')


# 노드의 개수
n = int(input())
tree = defaultdict()

# 이진 트리 만들기
for _ in range(n):
    value, left, right = input().split()
    tree[value] = Node(value, left, right)

preoder_traverse(tree['A'])
print()
inorder_traverse(tree['A'])
print()
postorder_traverse(tree['A'])
