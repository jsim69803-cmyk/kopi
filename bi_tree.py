class tree_node:
    def __init__(self):
        self.left = None
        self.data = None
        self.right = None

node1 = tree_node()
node1.data = "커피"

node2 = tree_node()
node2.data = "우유"
node1.left = node2

node3 = tree_node()
node3.data = "주스"
node1.right = node3

node4 = tree_node()
node4.data = "물"
node2.left = node4

node5 = tree_node()
node5.data = "콜라"
node2.right = node5

node6 = tree_node()
node6.data = "사이다"
node3.left = node6

print("=== 이진 트리 구조 ===")
print(node1.data, end=" ")
print()
print(node1.left.data, node1.right.data, end=" ")
print()
print(node1.left.left.data, node1.left.right.data, node1.right.left.data)
